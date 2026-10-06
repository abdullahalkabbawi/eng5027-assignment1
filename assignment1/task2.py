"""Task 2 (20%): enhance each recording by multiplying its FFT by a gain curve, then IFFT.

Owner: B. Run: python3 task2.py
"""
import matplotlib.pyplot as plt
import numpy as np

from common import WAV_5CM, WAV_1M, load_wav, save_wav, spectrum, save_fig


def enhance(path, label):
    fs, x = load_wav(path)
    X, f = spectrum(x, fs)

    # TODO: build a gain curve G(f) from corner frequencies justified by the Task 1 plots.
    # - define it on |f| so the negative-frequency mirror gets the same gain (real output)
    # - use smooth (e.g. raised-cosine) edges, not brick walls
    # - address the noise band, bass loss at 1 m and pops at 5 cm
    G = 1.0

    y = np.fft.ifft(X * G).real

    # TODO: before/after spectrum plot, gain curve on a twin axis (ax.twinx()),
    # save_fig(fig, "task2_..._" + label), save_wav(...) to listen to the result.


enhance(WAV_5CM, "5cm")
enhance(WAV_1M, "1m")
plt.show()
