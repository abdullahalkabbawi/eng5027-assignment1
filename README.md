# ENG5027 Assignment 1: Fourier Transform (group repo)

**Deadline: Monday 19 October, 3pm, on Moodle.** Aim to submit by noon.

| Task | Marks | What |
|---|---|---|
| 1 | 20% | Time and dB/log-frequency spectra of both recordings; mark vowel fundamentals, consonant band and noise-only region **by eye** |
| 2 | 20% | Enhance each recording by multiplying its FFT by a gain curve; explain noise, bass loss at 1 m and pops at 5 cm |
| 3 | 60% | Aural exciter for the 5 cm recording, shown as iterations (v1, v2, v3…) with at least two annotated graphs |

## Rules that cost all the marks for a part

- **Only `np.fft.fft`, `np.fft.ifft`, `np.fft.fftfreq`** for spectral work, plus plain NumPy,
  `scipy.io.wavfile` and Matplotlib. No `scipy.signal`, no FIR/IIR, no convolution as a filter,
  no peak finders or audio-effect libraries.
- **No automatic detection in Task 1.** Read the peaks off the plot yourselves.
- Recordings ≥ 44.1 kHz, uncompressed, not clipped.
- **Figures must be PDF/SVG.** Screenshots and JPEGs are not marked.
- Markers run the scripts **on Linux** with `python3 taskN.py`. Code that crashes or shows no
  plots loses most of the marks.

## Who does what

| Person | Owns | Also |
|---|---|---|
| A | Recordings, Task 1 | Repo; checks every script runs from a fresh terminal |
| B | Task 2 | Report editor (consistent style, final PDF) |
| C | Task 3 code (side chain, non-linearity, mix) | Reviews Task 1 |
| D | Task 3 experiments (version log, figures, listening at matched peak level) | GenAI statement; reviews Task 2 |

**Everyone must be able to explain every line of code**, because the markers may interview
any of us. On Fri 16 Oct each owner walks the others through their script.

## Schedule

| Date | Goal |
|---|---|
| Tue 6 Oct | Group in Moodle Wiki (names + matric numbers); Moodle naming rules copied below; repo and Overleaf ready |
| Wed 7 | Recordings re-done and checked (`python3 check_recordings.py`) |
| Thu 8 – Fri 9 | Task 1 plots and annotations; Task 2 FFT → gain → IFFT code; exciter v1 |
| Sat 10 – Sun 11 | Task 2 corner frequencies from the Task 1 plots; exciter v2; Task 1 written up |
| Mon 12 – Thu 15 | Exciter v3, v4 and final figures (A and B help with listening); Task 2 written up |
| Fri 16 | Code freeze, code walkthrough |
| Sat 17 | Full draft |
| Sun 18 | Everyone reads the whole report; scripts tested from a fresh terminal; zip built |
| Mon 19, by noon | Submit |

## Moodle naming conventions

TODO: copy them here exactly, then rename the WAVs and update every script that opens them
(including `check_recordings.py`).

## Layout

```
assignment1/            # this folder (code + WAVs) is what goes in the zip
    common.py           # shared helpers, written by the group
    check_recordings.py # sample rate, format, peak level, clipping
    task1.py task2.py task3.py
    voice_5cm.wav voice_1m.wav
    figures/            # PDFs written by the scripts, used by the report
report.tex              # main LaTeX file
sections/               # one file per section, so we can edit in parallel
```

## Running the code

```bash
cd assignment1
python3 check_recordings.py
python3 task1.py
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
- Figure names like `task1_spectrum_5cm.pdf`; axes labelled with units.

## Working with Git

- Pull before you start, commit small, push when it runs.
- Only edit your own task script and section file unless you've agreed otherwise.
  Changes to `common.py` affect everyone, so say so in the group chat first.
