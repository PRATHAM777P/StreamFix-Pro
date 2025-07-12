# StreamFix Pro

A robust tool to clean and deduplicate streamer rankings in JSON data, with CLI, logging, summary reporting, and modular code structure. Suitable for both CLI and web (Flask) integration.

## Features
- Deduplicates top N streamer IDs per section
- Customizable N (not just top 3)
- Section filtering
- Flexible input/output file names
- Output formats: JSON, pretty JSON, CSV
- Logging of all duplicate removals and errors
- Summary report (console and file, JSON or text)
- Robust error handling
- Unit tests for core logic
- Test case generator for stress testing
- Modular code for easy extension (e.g., Flask web interface)

## Usage

### CLI
```sh
python stream_rank_fixer.py -i input.json -o output.json -n 3 --format pretty --sections "Section_1" "Section_2" --summary-file summary.json
```
- `-i`, `--input`: Input JSON file
- `-o`, `--output`: Output file (JSON/CSV)
- `-n`, `--top_n`: Number of unique top streamers (default: 3)
- `--format`: Output format (`json`, `pretty`, `csv`)
- `-s`, `--sections`: Section names to process (default: all)
- `--summary-file`: Write summary report to file (JSON or TXT)

### Test Case Generator
Generate random test data for stress testing:
```sh
python test_case_generator.py -s 5 -n 30 -d 0.4 -o test_input.json
```

### Unit Tests
Run all tests:
```sh
python -m unittest test_stream_rank_fixer.py
```

## Privacy & GitHub
- No sensitive or personal data is stored or logged.
- All logs are local and can be deleted at any time.
- The codebase is modular and ready for open-source sharing.
- Please review and remove any test data before uploading to public repositories.

## Extending
- The code is modular and ready for Flask web integration and visualization (see TODOs).

---
For questions or contributions, please open an issue or pull request. 