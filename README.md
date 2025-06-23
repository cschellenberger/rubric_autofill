# Rubric Autofill

A helper tool to automate filling Brightspace rubric criteria from a CSV file.

## Features
- GUI file picker for CSV
- Automated keystrokes to fill rubric fields
- Clipboard integration
- Error handling and user prompts

## Usage
1. Run the application (no activation needed):
   ```powershell
   .\.venv\Scripts\python.exe -m src.rubric_autofill
   ```

## Setup
1. Create a virtual environment:
   ```powershell
   py -m venv .venv
   ```
2. Install dependencies:
   ```powershell
   .\.venv\Scripts\python.exe -m pip install -r requirements.txt
   ```

## Dependencies
- pyautogui
- pyperclip
- tkinter (standard library)

## Project Structure
- `src/` — main source code
- `rubric_autofill.py` — main script (moved to `src/`)
- `.venv/` — virtual environment
- `requirements.txt` — dependencies

---
Inspired by [attendance_autofill](https://github.com/cschellenberger/attendance_autofill)
