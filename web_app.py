from flask import Flask, request, render_template_string, send_file
import os
import tempfile
import json
from streamfix_pro import (
    load_input, save_output, process_sections, save_summary
)
import plotly.graph_objs as go
import plotly.io as pio
import base64

app = Flask(__name__)

HTML = '''
<!doctype html>
<title>StreamFix Pro Web</title>
<h2>StreamFix Pro Web Interface</h2>
<form method=post enctype=multipart/form-data>
  <label>Upload input JSON file:</label><br>
  <input type=file name=input_file required><br><br>
  <label>Top N unique streamers:</label>
  <input type=number name=top_n value=3 min=1 required><br><br>
  <label>Section filter (comma separated, optional):</label>
  <input type=text name=sections><br><br>
  <label>Output format:</label>
  <select name=format>
    <option value="json">JSON</option>
    <option value="pretty">Pretty JSON</option>
    <option value="csv">CSV</option>
  </select><br><br>
  <input type=submit value="Process">
</form>
{% if output_url %}
  <h3>Download Results:</h3>
  <a href="{{ output_url }}">Download Cleaned Output</a><br>
  <a href="{{ summary_url }}">Download Summary Report</a><br><br>
  <form method="post">
    <input type="hidden" name="input_json" value="{{ input_json }}">
    <input type="hidden" name="output_json" value="{{ output_json }}">
    <input type="hidden" name="top_n" value="{{ top_n }}">
    <input type="hidden" name="sections" value="{{ sections }}">
    <input type="submit" name="visualize" value="Show Before/After Visualization">
  </form>
{% endif %}
{% if plot_img %}
  <h3>Before/After Unique Streamers in Top N</h3>
  <img src="data:image/png;base64,{{ plot_img }}"/>
{% endif %}
''' 

def get_unique_counts(data, top_n, sections=None):
    counts = {}
    for section in data:
        section_id = section.get('sectionID')
        if not section_id:
            continue
        if sections and section_id not in sections:
            continue
        section_data = section.get('sectionData', [])
        top_ids = [item['streamerID'] for item in section_data[:top_n]]
        counts[section_id] = len(set(top_ids))
    return counts

@app.route('/', methods=['GET', 'POST'])
def index():
    output_url = summary_url = plot_img = None
    input_json = output_json = ''
    top_n = 3
    sections = ''
    if request.method == 'POST':
        if 'visualize' in request.form:
            # Visualization request
            input_json = request.form['input_json']
            output_json = request.form['output_json']
            top_n = int(request.form['top_n'])
            sections = request.form['sections']
            section_list = [s.strip() for s in sections.split(',') if s.strip()] if sections else None
            input_data = json.loads(input_json)
            output_data = json.loads(output_json)
            before_counts = get_unique_counts(input_data, top_n, section_list)
            after_counts = {k: len(set(v[:top_n])) for k, v in output_data.items() if (not section_list or k in section_list)}
            section_names = list(before_counts.keys())
            before = [before_counts.get(s, 0) for s in section_names]
            after = [after_counts.get(s, 0) for s in section_names]
            fig = go.Figure(data=[
                go.Bar(name='Before', x=section_names, y=before),
                go.Bar(name='After', x=section_names, y=after)
            ])
            fig.update_layout(barmode='group', title=f'Unique Streamers in Top {top_n} (Before/After)')
            img_bytes = pio.to_image(fig, format='png')
            plot_img = base64.b64encode(img_bytes).decode('utf-8')
            return render_template_string(HTML, output_url=None, summary_url=None, plot_img=plot_img, input_json=input_json, output_json=output_json, top_n=top_n, sections=sections)
        # Normal process request
        file = request.files['input_file']
        if not file:
            return render_template_string(HTML, output_url=None, summary_url=None, plot_img=None)
        top_n = int(request.form.get('top_n', 3))
        fmt = request.form.get('format', 'json')
        sections = request.form.get('sections', '').strip()
        section_list = [s.strip() for s in sections.split(',') if s.strip()] if sections else None
        # Save uploaded file to temp
        with tempfile.NamedTemporaryFile(delete=False, suffix='.json') as tmp_in:
            file.save(tmp_in)
            tmp_in_path = tmp_in.name
        # Prepare output files
        tmp_out = tempfile.NamedTemporaryFile(delete=False, suffix=f'.{fmt}')
        tmp_sum = tempfile.NamedTemporaryFile(delete=False, suffix='.json')
        try:
            data = load_input(tmp_in_path)
            output, summary = process_sections(data, top_n, section_list)
            save_output(output, tmp_out.name, fmt)
            save_summary(summary, tmp_sum.name, top_n)
            output_url = f'/download/{os.path.basename(tmp_out.name)}'
            summary_url = f'/download/{os.path.basename(tmp_sum.name)}'
            # For visualization, pass JSON as hidden fields
            input_json = json.dumps(data)
            output_json = json.dumps(output)
        except Exception as e:
            return f'<h3>Error: {e}</h3>'
        finally:
            os.unlink(tmp_in_path)
    return render_template_string(HTML, output_url=output_url, summary_url=summary_url, plot_img=plot_img, input_json=input_json, output_json=output_json, top_n=top_n, sections=sections)

@app.route('/download/<filename>')
def download_file(filename):
    dirpath = tempfile.gettempdir()
    return send_file(os.path.join(dirpath, filename), as_attachment=True)

if __name__ == '__main__':
    app.run(debug=True) 