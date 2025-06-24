# Rubric Autofill

A helper tool to automate filling Brightspace rubric criteria using data from a CSV file. The script simulates keystrokes to paste values into the Brightspace rubric form, making the process faster and less error-prone.

## Features
- GUI file picker for CSV selection
- Modal dialog to prompt user to focus the first rubric field
- Simulates keystrokes for each row in the CSV:
  - Pastes each field into the rubric form
  - Navigates using Tab keys as required by Brightspace
- Skips blank lines and validates column count
- User-friendly error and completion dialogs

## Usage
1. Run the script:
   ```sh
   python -m src.rubric_autofill
   ```
2. Select your CSV file when prompted.
3. Place the cursor in the first criterion label field in Brightspace and click "Start".
4. The script will autofill the rubric fields row by row.

## CSV Format
Each row must have **7 columns**:
1. Criterion label
2. Standard 1
3. Standard 2
4. Standard 3
5. Feedback 1
6. Feedback 2
7. Feedback 3

Blank lines are ignored. Any row with a different number of columns will cause an error.

## Requirements
- Windows OS
- Python 3.8+
- Brightspace open in your browser

## Installation
1. Create a virtual environment (optional but recommended):
   ```sh
   python -m venv .venv
   .venv\Scripts\activate
   ```
2. Install dependencies:
   ```sh
   pip install -r requirements.txt
   ```

## Building a Windows Executable

You can create a standalone `.exe` using [PyInstaller](https://pyinstaller.org/):

1. Install PyInstaller in your virtual environment:
   ```sh
   pip install pyinstaller
   ```
2. Build the executable:
   ```sh
   pyinstaller --onefile --noconsole src/rubric_autofill.py -n rubric_autofill
   ```
   - The `.exe` will be in the `dist/` folder as `rubric_autofill.exe`.

3. (Optional) Test the executable by running it directly:
   ```sh
   dist\rubric_autofill.exe
   ```

## Publishing to GitHub Releases

1. Commit and push the `dist/rubric_autofill.exe` file to your repository (or preferably, upload it as a Release asset on GitHub).
2. On GitHub, go to the Releases section and create a new release. Attach the `.exe` file for users to download.

## Notes
- The script uses `pyautogui` to simulate keystrokes and `pyperclip` for clipboard operations. Make sure your system allows these actions.
- Increase the delays in the script if you experience reliability issues.

## License
See [LICENSE.txt](LICENSE.txt).
