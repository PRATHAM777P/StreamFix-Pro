<h1 align="center">StreamFix Pro</h1>
<p align="center">
  <b>Clean, deduplicate, and visualize streamer rankings with ease!</b><br><br>
  <a href="#features">Features</a> •
  <a href="#quick-start">Quick Start</a> •
  <a href="#usage">Usage</a> •
  <a href="#unit-tests">Tests</a> •
  <a href="#project-structure">Structure</a> •
  <a href="#extending">Extending</a>
</p>
<p align="center">
  <img src="https://img.shields.io/badge/Python-3.7%2B-blue" alt="Python Version">
  <img src="https://img.shields.io/badge/Web-Interface-brightgreen" alt="Web Interface">
  <img src="https://img.shields.io/badge/CLI-Supported-blueviolet" alt="CLI Supported">
  <img src="https://img.shields.io/badge/Tests-Unittest-orange" alt="Tests">
</p>

---

## 🚀 Quick Start

1. **Clone the repo:**
   ```sh
   git clone https://github.com/yourusername/streamfix-pro.git
   cd streamfix-pro
   ```

2. **Install dependencies:**
   ```sh
   pip install -r requirements.txt
   ```

3. **Run the web app:**
   ```sh
   python web_app.py
   ```
   Then open [http://127.0.0.1:5000](http://127.0.0.1:5000) in your browser.

---

## ✨ Features

- 🏆 **Deduplicate top N streamer IDs** per section
- 🔢 **Customizable N** — not just top 3, any number you want
- 🗂️ **Section filtering** — process only the sections you need
- 📂 **Flexible input/output** file names
- 📝 **Multiple output formats** — JSON, pretty JSON, CSV
- 🪵 **Logging** of all duplicate removals and errors (local only)
- 📊 **Summary report** — console and file output (JSON or TXT)
- 🛡️ **Robust error handling** throughout
- 🧪 **Unit tests** for all core logic
- 🧰 **Test case generator** for stress testing
- 🌐 **Web interface** — upload, process, download, and visualize with Plotly

---

## 📖 Usage

### CLI
```sh
python streamfix_pro.py -i input.json -o output.json -n 3 --format pretty --sections "Section_1" "Section_2" --summary-file summary.json
```

| Argument | Description | Default |
|---|---|---|
| `-i`, `--input` | Input JSON file | `input.json` |
| `-o`, `--output` | Output file (JSON/CSV) | `output.json` |
| `-n`, `--top_n` | Number of unique top streamers | `3` |
| `--format` | Output format: `json`, `pretty`, `csv` | `json` |
| `-s`, `--sections` | Section names to process | all |
| `--summary-file` | Write summary report to file (JSON or TXT) | none |

---

### Web Interface
```sh
python web_app.py
```
Then open [http://127.0.0.1:5000](http://127.0.0.1:5000) in your browser.

- Upload your JSON file
- Set Top N and section filters
- Download cleaned output and summary
- View Before/After visualization chart

---

### Test Case Generator
Generate random test data for stress testing:
```sh
python test_case_generator.py -s 5 -n 30 -d 0.4 -o test_input.json
```

| Argument | Description | Default |
|---|---|---|
| `-s` | Number of sections | `3` |
| `-n` | Streams per section | `20` |
| `-d` | Duplicate probability (0.0 - 1.0) | `0.3` |
| `-o` | Output file name | `input.json` |

---

## 🧪 Unit Tests
Run all tests:
```sh
python -m unittest test_streamfix_pro.py
```

Tests cover:
- ✅ No duplicates needed
- ✅ Duplicates in top N
- ✅ Less data than N
- ✅ Empty input
- ✅ Summary tracking

---

## 📁 Project Structure

```
streamfix-pro/
│
├── streamfix_pro.py         # Core logic
├── web_app.py               # Flask web interface
├── test_case_generator.py   # Random test data generator
├── test_streamfix_pro.py    # Unit tests
├── requirements.txt         # Dependencies
└── .gitignore               # Git ignore rules
```

---

## 🛠️ Extending

The code is fully modular and easy to extend:
- Add new output formats in `save_output()`
- Add new routes to `web_app.py`
- Add more test cases in `test_streamfix_pro.py`

---

## 📦 Dependencies

| Package | Purpose |
|---|---|
| `flask` | Web interface |
| `plotly` | Before/After visualization |
| `werkzeug` | Secure file downloads |
| `kaleido` | Plotly image export |

---

<p align="center">
  <i>For questions or contributions, please open an issue or pull request.</i>
</p>
