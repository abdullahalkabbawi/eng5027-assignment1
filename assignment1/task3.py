"""Task 3 (60%): aural exciter for the 5 cm recording, built only with FFT/IFFT and NumPy.

Owners: C (code) and D (experiments, figures). Run: python3 task3.py

Keep every version's parameters in VERSIONS so the report can show the iterations
(observed -> changed -> result) and the version-comparison figure can be regenerated.
"""
import matplotlib.pyplot as plt

from common import WAV_5CM, load_wav, spectrum, save_fig

VERSIONS = {
    # name: parameters. Change one thing per version and log why in the report.
    "v1": dict(band=(2000, 5000), drive=5.0, mix=0.1),
}


def exciter(x, fs, band, drive, mix):
    # TODO: dry path + side chain:
    #   1. band-pass the side chain by editing FFT coefficients (smooth edges)
    #   2. non-linearity (e.g. tanh(drive * s)) to create harmonics
    #   3. keep the harmonic band you want, again in the FFT domain
    #   4. add mix * side chain to the dry signal
    raise NotImplementedError


fs, x = load_wav(WAV_5CM)
for name, params in VERSIONS.items():
    pass  # TODO: y = exciter(x, fs, **params); normalise to the same peak as x before
          # listening/plotting (louder always sounds "better"); save figures and WAVs.

plt.show()
