# ENG5027 Assignment 1: Fourier Transform (group repo)

**Deadline: Monday 19 October, 3pm, on Moodle.** Aim to submit by noon.

The official brief is [`assignment-brief.pdf`](assignment-brief.pdf). Check every script and
the report against it before merging. If anything in this README disagrees with it, the brief
wins.

| Task | Marks | What |
|---|---|---|
| 1 | 20% | Time and dB/log-frequency spectra of both recordings; mark vowel fundamentals, consonant band and noise-only region **by eye** |
| 2 | 20% | Enhance each recording by multiplying its FFT by a gain curve; explain noise, bass loss at 1 m and pops at 5 cm |
| 3 | 60% | Aural exciter for the 5 cm recording, shown as iterations (v1, v2, v3…) with at least two annotated graphs |

## Rules that cost all the marks for a part

- **Only `np.fft.fft` and `np.fft.ifft`** for signal processing. Not even `np.fft.fftfreq`
  (the brief names it explicitly): build the frequency axis yourself with plain NumPy. No
  `scipy.signal`, no FIR/IIR, no convolution as a filter, no peak finders or audio-effect
  libraries. Any of these gives **zero for that part**.
- **No automatic detection in Task 1.** Read the peaks off the plot yourselves.
- Recordings ≥ 44 kHz, uncompressed, not clipped, full spectrum up to 20 kHz.
- **Figures must be vector (PDF/SVG).** Screenshots and JPEGs are not marked. Report is PDF.

## Rules that cost marks

- Markers run the scripts **on Linux from the command line** (`python3 audioplot.py`,
  `python3 auralexciter.py`). Code that crashes or shows no plots gets low marks. No absolute
  paths; platform-independent. The markers get only the seven files in the zip, all in one
  folder: the scripts must find the WAVs next to themselves, and create any folder they save
  figures into (`os.makedirs(..., exist_ok=True)`).
- **Efficient code**: don't compute a huge spectrum to use one value.
- **Short, readable code.** Inflated or unreadable LLM-style code gets low or zero marks; every
  task can be solved in very few lines.
- **GenAI acknowledgement** in the report if any GenAI was used: tool name, version, publisher,
  how it was used, and what you did yourselves.
- The markers may **interview** you to check you can explain your code.

## Team 37

| Name | Matric | Role |
|---|---|---|
| Nommy Khodadad | 3184012K | TODO |
| Parth Sheetal Kumthekar | 3183509K | TODO |
| Abdullah Alkabbawi | 2560946A | A (voice in the recordings) |
| Seyedmostafa Hosseini Abardeh | 3184088H | TODO |

Submission zip: `3184012k_3183509k_2560946a_3184088h.zip`

## Who does what

| Person | Owns | Also |
|---|---|---|
| A | Recordings, Part 1 (in `audioplot.py`) | Repo; checks every script runs from a fresh terminal |
| B | Part 2 (in `audioplot.py`, writes the enhanced WAVs) | Report editor (consistent style, final PDF) |
| C | Part 3 code in `auralexciter.py` (side chain, non-linearity, mix) | Reviews Part 1 |
| D | Part 3 experiments (version log, figures, listening at matched peak level) | GenAI statement; reviews Part 2 |

**Everyone must be able to explain every line of code**, because the markers may interview
any of us. On Fri 16 Oct each owner walks the others through their script.

## Schedule

| Date | Goal |
|---|---|
| Tue 6 Oct | Group in Moodle Wiki (names + matric numbers); Moodle naming rules copied below; repo and Overleaf ready |
| Wed 7 | Recordings re-done, saved as `original_speech_5cm.wav` / `original_speech_1m.wav`, checked (`python3 tools/check_recordings.py`) |
| Thu 8 – Fri 9 | Task 1 plots and annotations; Task 2 FFT → gain → IFFT code; exciter v1 |
| Sat 10 – Sun 11 | Task 2 corner frequencies from the Task 1 plots; exciter v2; Task 1 written up |
| Mon 12 – Thu 15 | Exciter v3, v4 and final figures (A and B help with listening); Task 2 written up |
| Fri 16 | Code freeze, code walkthrough |
| Sat 17 | Full draft |
| Sun 18 | Everyone reads the whole report; scripts tested from a fresh terminal; zip built (`python3 tools/make_submission.py`) |
| Mon 19, by noon | Submit |

## Moodle submission

One `.zip` named with our four matric numbers, e.g.
`1234567a_7654321b_2468246a_6428642b.zip`, containing exactly:

| File | What |
|---|---|
| `report.pdf` | The report |
| `original_speech_5cm.wav` | Original speech recorded at 5 cm |
| `original_speech_1m.wav` | Original speech recorded at 1 m |
| `enhanced_speech_5cm.wav` | Enhanced speech at 5 cm (written by `audioplot.py`) |
| `enhanced_speech_1m.wav` | Enhanced speech at 1 m (written by `audioplot.py`) |
| `audioplot.py` | Parts 1 and 2 |
| `auralexciter.py` | Part 3 |

`tools/make_submission.py` builds it: fill in the matric numbers, save the Overleaf PDF as
`report.pdf` in the repo root, run `audioplot.py`, then run the tool. It stops if a file is
missing.

## Layout

```
assignment-brief.pdf    # the official assignment sheet: check everything against it
assignment1/            # code + WAVs that go in the zip
    audioplot.py        # Parts 1 and 2 (A and B)
    auralexciter.py     # Part 3 (C and D)
    original_speech_5cm.wav original_speech_1m.wav
    enhanced_speech_5cm.wav enhanced_speech_1m.wav   # written by audioplot.py
    figures/            # PDFs written by the scripts, used by the report (not submitted)
tools/                  # helpers for us, not submitted
    check_recordings.py # sample rate, format, peak level, clipping
    make_submission.py  # builds the Moodle zip
report.tex              # main LaTeX file
sections/               # one file per section, so we can edit in parallel
```

## Running the code

```bash
python3 tools/check_recordings.py
cd assignment1
python3 audioplot.py
python3 auralexciter.py
```

Requires `numpy`, `scipy` and `matplotlib` only. Keep every file name lower case, because Linux
is case-sensitive.

## Report

- Upload the whole repo to Overleaf (New Project → Upload Project with a zip of the repo), or
  build locally with `pdflatex report.tex`. Figures and the code appendix are read straight
  from `assignment1/`, so re-run the scripts and recompile to update them.
- Order: Introduction (two lines) → Task 1 → Task 2 → Task 3 → GenAI acknowledgement →
  Appendix (complete code).
- Brief and technical: method, result and *why*. No textbook theory.
- Figure names like `part1_spectrum_5cm.pdf`; axes labelled with units.
- Download the compiled PDF from Overleaf and save it as `report.pdf` in the repo root.

## Working with Git

- Pull before you start, commit small, push when it runs.
- Only edit your own part and section file unless you've agreed otherwise. A and B share
  `audioplot.py`: keep to your own `# ---- Part N ----` block and pull right before editing.
