import json
import argparse
import logging

# Input parsing

def parse_args():
    parser = argparse.ArgumentParser(description='Fix top N unique streamers per section.')
    parser.add_argument('-i', '--input', default='input.json', help='Input JSON file')
    parser.add_argument('-o', '--output', default='output.json', help='Output JSON file')
    parser.add_argument('-n', '--top_n', type=int, default=3, help='Number of unique top streamers')
    parser.add_argument('-s', '--sections', nargs='*', help='Section names to process (default: all)')
    parser.add_argument('--format', choices=['json', 'pretty', 'csv'], default='json', help='Output format')
    parser.add_argument('--summary-file', help='Optional file to write summary report (JSON or TXT based on extension)')
    return parser.parse_args()

def load_input(input_file):
    with open(input_file, 'r') as f:
        return json.load(f)

def save_output(output, output_file, fmt):
    with open(output_file, 'w') as f:
        if fmt == 'json':
            json.dump(output, f)
        elif fmt == 'pretty':
            json.dump(output, f, indent=2)
        elif fmt == 'csv':
            import csv
            writer = csv.writer(f)
            for section, ids in output.items():
                writer.writerow([section] + ids)

def save_summary(summary, summary_file, top_n):
    if summary_file.lower().endswith('.json'):
        with open(summary_file, 'w') as sf:
            json.dump(summary, sf, indent=2)
    else:
        with open(summary_file, 'w') as sf:
            sf.write(f"Summary of duplicates moved out of top {top_n}:\n")
            for section, count in summary.items():
                sf.write(f"  {section}: {count} duplicates moved out of top {top_n}\n")

def setup_logging():
    logging.basicConfig(
        filename='stream_rank_fixer.log',
        filemode='a',
        format='%(asctime)s %(levelname)s: %(message)s',
        level=logging.INFO
    )

def fix_top_n_no_duplicates(section_data, top_n, section_id=None, summary=None):
    streamer_ids = [item['streamerID'] for item in section_data]
    seen = set()
    fixed_top = []
    idx = 0
    moved = []
    # Fill top N with unique IDs
    while len(fixed_top) < top_n and idx < len(streamer_ids):
        if streamer_ids[idx] not in seen:
            fixed_top.append(streamer_ids[idx])
            seen.add(streamer_ids[idx])
        else:
            moved.append((idx, streamer_ids[idx]))
        idx += 1
    # If still less than N, fill with whatever is left
    for i in range(top_n):
        if len(fixed_top) < top_n and i < len(streamer_ids):
            if streamer_ids[i] not in fixed_top:
                fixed_top.append(streamer_ids[i])
            else:
                moved.append((i, streamer_ids[i]))
    # Build the rest of the list (from N onward)
    rest = []
    for i in range(top_n, len(streamer_ids)):
        rest.append(streamer_ids[i])
    # Logging
    if section_id is not None:
        for idx, sid in moved:
            logging.info(f"Section '{section_id}': Duplicate streamerID '{sid}' at position {idx+1} moved out of top {top_n}.")
        if summary is not None:
            summary[section_id] = summary.get(section_id, 0) + len(moved)
    return fixed_top + rest

def process_sections(data, top_n, sections=None):
    output = {}
    summary = {}
    for section in data:
        section_id = section.get('sectionID')
        if not section_id:
            continue
        if sections and section_id not in sections:
            continue
        section_data = section.get('sectionData', [])
        fixed_streams = fix_top_n_no_duplicates(section_data, top_n, section_id, summary)
        output[section_id] = fixed_streams
    return output, summary

def main():
    setup_logging()
    args = parse_args()
    try:
        data = load_input(args.input)
    except Exception as e:
        logging.error(f"Error reading input file: {e}")
        print(f"Error reading input file: {e}")
        return
    try:
        output, summary = process_sections(data, args.top_n, args.sections)
    except Exception as e:
        logging.error(f"Error processing sections: {e}")
        print(f"Error processing sections: {e}")
        return
    try:
        save_output(output, args.output, args.format)
    except Exception as e:
        logging.error(f"Error writing output file: {e}")
        print(f"Error writing output file: {e}")
        return
    print("Summary of duplicates moved out of top N:")
    for section, count in summary.items():
        print(f"  {section}: {count} duplicates moved out of top {args.top_n}")
    if args.summary_file:
        try:
            save_summary(summary, args.summary_file, args.top_n)
        except Exception as e:
            logging.error(f"Error writing summary file: {e}")
            print(f"Error writing summary file: {e}")

if __name__ == '__main__':
    main() 