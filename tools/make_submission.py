"""Build the Moodle zip: exactly the seven files Moodle asks for, flat, named by matric numbers.

1. Fill in MATRIC below.
2. Download the compiled report from Overleaf and save it as report.pdf in the repo root.
3. Run audioplot.py so the enhanced WAVs exist.
4. Run from anywhere: python3 tools/make_submission.py
"""
import os
import sys
import zipfile

MATRIC = []  # TODO: our four matric numbers, e.g. ["1234567a", "7654321b", ...]

ROOT = os.path.join(os.path.dirname(os.path.abspath(__file__)), "..")
CODE = os.path.join(ROOT, "assignment1")
FILES = {
    "report.pdf": ROOT,
    "original_speech_5cm.wav": CODE,
    "original_speech_1m.wav": CODE,
    "enhanced_speech_5cm.wav": CODE,
    "enhanced_speech_1m.wav": CODE,
    "audioplot.py": CODE,
    "auralexciter.py": CODE,
}

if len(MATRIC) != 4:
    sys.exit("Fill in the four matric numbers in MATRIC first.")

missing = [name for name, folder in FILES.items() if not os.path.isfile(os.path.join(folder, name))]
if missing:
    sys.exit("Missing: " + ", ".join(missing))

zip_path = os.path.join(ROOT, "_".join(MATRIC) + ".zip")
with zipfile.ZipFile(zip_path, "w", zipfile.ZIP_DEFLATED) as z:
    for name, folder in FILES.items():
        z.write(os.path.join(folder, name), name)
print("Wrote", os.path.normpath(zip_path))
