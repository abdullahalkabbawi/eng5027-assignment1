"""Task 1 (20%): time and frequency plots of both recordings, annotated by eye.

Owner: A. Run: python3 task1.py
"""
import matplotlib.pyplot as plt
import numpy as np

from common import WAV_5CM, WAV_1M, load_wav, spectrum, positive_half, to_db, save_fig


def analyse(path, label):
    fs, x = load_wav(path)
    t = np.arange(len(x)) / fs

    # (i) Time domain
    fig, ax = plt.subplots()
    ax.plot(t, x, linewidth=0.5)
    ax.set(xlabel="Time (s)", ylabel="Normalised amplitude", title=label + " recording")
    save_fig(fig, "task1_time_" + label)

    # (ii) Frequency domain: log frequency axis, amplitude in dB
    X, f = positive_half(*spectrum(x, fs))
    fig, ax = plt.subplots()
    ax.semilogx(f, to_db(X), linewidth=0.5)
    ax.set(xlabel="Frequency (Hz)", ylabel="Magnitude (dB)", title=label + " spectrum")

    # TODO (iii) vowel fundamentals, (iv) consonant range, (v) noise-only region:
    # read them off the plot yourself (no automatic detection), then mark them with
    # ax.axvspan / ax.annotate and justify each choice in the report.

    save_fig(fig, "task1_spectrum_" + label)


analyse(WAV_5CM, "5cm")
analyse(WAV_1M, "1m")
plt.show()
