"""Shared helpers for Tasks 1-3: loading the recordings, computing spectra, saving figures.

Only numpy, scipy.io.wavfile and matplotlib are used, and the only spectral functions are
np.fft.fft / np.fft.ifft / np.fft.fftfreq, as the brief requires.
"""
import os

import numpy as np
import matplotlib.pyplot as plt
from scipy.io import wavfile

HERE = os.path.dirname(os.path.abspath(__file__))
FIG_DIR = os.path.join(HERE, "figures")

# Change these once (here only) if Moodle asks for different file names.
WAV_5CM = os.path.join(HERE, "voice_5cm.wav")
WAV_1M = os.path.join(HERE, "voice_1m.wav")

# One look for every figure in the report.
plt.rcParams.update({
    "figure.figsize": (7, 3.6),
    "font.size": 10,
    "axes.grid": True,
    "grid.alpha": 0.3,
    "savefig.bbox": "tight",
})


def load_wav(path):
    """Return (fs, x) with x mono float, scaled so integer full scale = 1.0.

    Dividing by full scale (not by the signal's own peak) keeps the two recordings
    comparable: the 1 m one stays quieter.
    """
    fs, x = wavfile.read(path)
    if x.ndim > 1:
        x = x[:, 0]
    if np.issubdtype(x.dtype, np.integer):
        x = x / np.iinfo(x.dtype).max
    return fs, x.astype(float)


def save_wav(path, fs, x):
    """Write x (full scale = 1.0) as 16-bit PCM. Clips at +/-1, so normalise first."""
    x = np.clip(x, -1.0, 1.0)
    wavfile.write(path, fs, (x * 32767).astype(np.int16))


def spectrum(x, fs):
    """FFT of x. Returns (X, f): full complex spectrum and its bin frequencies in Hz.

    Keep the full X for filtering (edit X, then np.fft.ifft). For plotting, use
    positive_half(X, f) to drop the mirrored negative frequencies.
    """
    X = np.fft.fft(x)
    f = np.fft.fftfreq(len(x), 1 / fs)
    return X, f


def positive_half(X, f):
    """Bins with 0 < f < fs/2 (DC dropped so a log frequency axis works)."""
    keep = f > 0
    return X[keep], f[keep]


def to_db(X, ref=1.0):
    """Magnitude in dB relative to ref. The floor avoids log(0)."""
    return 20 * np.log10(np.maximum(np.abs(X), 1e-12) / ref)


def save_fig(fig, name):
    """Save fig as figures/<name>.pdf (vector, as the brief requires)."""
    os.makedirs(FIG_DIR, exist_ok=True)
    fig.savefig(os.path.join(FIG_DIR, name + ".pdf"))
