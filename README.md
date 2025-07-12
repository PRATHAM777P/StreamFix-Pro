<h1 align="center">StreamFix Pro</h1>

<p align="center">
  <b>Clean, deduplicate, and visualize streamer rankings with ease!</b><br>
  <a href="#features">Features</a> • <a href="#quick-start">Quick Start</a> • <a href="#usage">Usage</a> • <a href="#privacy--github">Privacy</a> • <a href="#extending">Extending</a>
</p>

<p align="center">
  <img src="https://img.shields.io/badge/Python-3.7%2B-blue" alt="Python Version">
  <img src="https://img.shields.io/badge/Web-Interface-brightgreen" alt="Web Interface">
  <img src="https://img.shields.io/badge/CLI-Supported-blueviolet" alt="CLI Supported">
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
   pip install flask plotly
   ```
3. **Run the web app:**
   ```sh
   python web_app.py
   ```
   Then open [http://127.0.0.1:5000](http://127.0.0.1:5000) in your browser.

---

## ✨ Features

- 🏆 **Deduplicate top N streamer IDs per section**
- 🔢 **Customizable N** (not just top 3)
- 🗂️ **Section filtering**
- 📂 **Flexible input/output file names**
- 📝 **Output formats:** JSON, pretty JSON, CSV
- 🪵 **Logging** of all duplicate removals and errors (local only)
- 📊 **Summary report** (console and file, JSON or text)
- 🛡️ **Robust error handling**
- 🧪 **Unit tests** for core logic
- 🧰 **Test case generator** for stress testing
- 🧩 **Modular code** for easy extension (e.g., Flask web interface)
- 🌐 **Web interface** for upload, download, and visualization (plotly)

---

## 📖 Usage

### CLI
```sh
python streamfix_pro.py -i input.json -o output.json -n 3 --format pretty --sections "Section_1" "Section_2" --summary-file summary.json
```
- `-i`, `--input`: Input JSON file
- `-o`, `--output`: Output file (JSON/CSV)
- `-n`, `--top_n`: Number of unique top streamers (default: 3)
- `--format`: Output format (`json`, `pretty`, `csv`)
- `-s`, `--sections`: Section names to process (default: all)
- `--summary-file`: Write summary report to file (JSON or TXT)

### Web Interface
```sh
python web_app.py
```
Then open [http://127.0.0.1:5000](http://127.0.0.1:5000) in your browser.

### Test Case Generator
Generate random test data for stress testing:
```sh
python test_case_generator.py -s 5 -n 30 -d 0.4 -o test_input.json
```

### Unit Tests
Run all tests:
```sh
python -m unittest test_streamfix_pro.py
```

---

## 🛠️ Extending
- The code is modular and ready for Flask web integration and visualization.

---

<p align="center">
  <i>For questions or contributions, please open an issue or pull request.</i>
</p>
