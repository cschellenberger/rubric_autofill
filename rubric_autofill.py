# rubric_autofill.py
# Brightspace “Rubric Criteria Group” autofill helper
#
# Keystroke pattern for *each* CSV row
#   1.  Ctrl+A  Ctrl+V  Tab  Tab                (criterion label)
#   2.  Ctrl+A  Ctrl+V  Tab                     (standard 1)
#   3.  Ctrl+A  Ctrl+V  Tab                     (standard 2)
#   4.  Ctrl+A  Ctrl+V  Tab                     (standard 3)
#   5.  Ctrl+A  Ctrl+V  Tab                     (feedback 1)
#   6.  Ctrl+A  Ctrl+V  Tab                     (feedback 2)
#   7.  Ctrl+A  Ctrl+V  Tab  Tab  Tab           (feedback 3 → jump to next crit.)
#
# ──────────────────────────────────────────────────────────────────────────────

# (This file is now a placeholder. The main script has been moved to src/rubric_autofill.py)

import csv
import time
from pathlib import Path

import pyautogui               # ⇢ keyboard / mouse
import pyperclip               # ⇢ clipboard copy
import tkinter as tk
from tkinter import filedialog, messagebox

# ------------------------------ Tuning --------------------------------------#
ROW_DELAY   = 0.20   # seconds to pause after finishing each row (increased for reliability)
PASTE_DELAY = 0.20   # increased pause after paste for maximum reliability
SELECT_PASTE_PAUSE = 0.15  # pause between select-all and paste
TAB_DELAY = 0.25    # pause after each tab key press
# ----------------------------------------------------------------------------#


def pick_csv() -> Path | None:
    """File-open dialog → Path (or None if cancelled)."""
    root = tk.Tk()
    root.withdraw()
    fp = filedialog.askopenfilename(
        title="Select Brightspace Rubric CSV",
        filetypes=[("CSV files", "*.csv"), ("All files", "*.*")]
    )
    root.destroy()
    return Path(fp) if fp else None


def wait_for_start() -> None:
    """Modal dialog telling user to focus the FIRST rubric field."""
    dlg = tk.Tk()
    dlg.title("Rubric Autofill – Ready?")
    dlg.resizable(False, False)

    tk.Label(
        dlg,
        text=("Place the text cursor in the FIRST criterion label field of "
              "your Brightspace rubric, then click ‘Start’."),
        wraplength=320, justify="left", padx=20, pady=15
    ).pack()

    tk.Button(dlg, text="Start", width=12, command=dlg.destroy).pack(pady=(0, 15))
    dlg.attributes("-topmost", True)
    dlg.mainloop()


def _paste(text: str) -> None:
    """Select-all ➜ pause ➜ paste `text` (using clipboard) into current field."""
    pyperclip.copy(text)
    pyautogui.hotkey("ctrl", "a")     # Select All
    time.sleep(SELECT_PASTE_PAUSE)      # Short pause between select-all and paste
    pyautogui.hotkey("ctrl", "v")     # Paste
    time.sleep(PASTE_DELAY)


def autofill(csv_path: Path) -> None:
    """Drive keystrokes for every row → Brightspace rubric form."""
    with csv_path.open(newline="", encoding="utf-8") as f:
        reader = csv.reader(f)
        for row_num, row in enumerate(reader, start=1):
            if not row:                               # skip blank lines
                continue

            fields_expected = 7
            if len(row) != fields_expected:
                raise ValueError(
                    f"Row {row_num} has {len(row)} columns; expected {fields_expected}."
                )

            for col_idx, cell in enumerate(row):
                # Step 1 (criterion): tabs afterwards
                if col_idx == 0:
                    _paste(cell)
                    pyautogui.press("tab", presses=2, interval=TAB_DELAY)
                    time.sleep(TAB_DELAY)
                # Step 7 (last feedback): three tabs afterwards (not four)
                elif col_idx == len(row) - 1:
                    _paste(cell)
                    pyautogui.press("tab", presses=3, interval=TAB_DELAY)
                    time.sleep(TAB_DELAY)
                # Middle fields: single tab afterwards
                else:
                    _paste(cell)
                    pyautogui.press("tab", interval=TAB_DELAY)
                    time.sleep(TAB_DELAY)

            time.sleep(ROW_DELAY)


if __name__ == "__main__":
    csv_file = pick_csv()
    if not csv_file:
        messagebox.showinfo("Rubric Autofill", "No file selected – exiting.")
        raise SystemExit

    wait_for_start()            # user positions cursor & clicks “Start”

    try:
        autofill(csv_file)
        messagebox.showinfo("Rubric Autofill", "✅ Rubric autofill complete.")
    except Exception as exc:
        messagebox.showerror("Rubric Autofill", f"⚠ An error occurred:\n{exc}")
