"""Check both recordings meet the marking rules: >= 44.1 kHz, uncompressed PCM, not clipped.

Run: python3 check_recordings.py
"""
import numpy as np
from scipy.io import wavfile

from common import WAV_5CM, WAV_1M

for path in (WAV_5CM, WAV_1M):
    fs, x = wavfile.read(path)
    full_scale = np.iinfo(x.dtype).max if np.issubdtype(x.dtype, np.integer) else 1.0
    a = np.abs(x.astype(float))
    peak = a.max() / full_scale
    clipped = int(np.sum(a >= full_scale))
    print("%s\n  fs = %d Hz, dtype = %s, shape = %s, duration = %.2f s"
          % (path, fs, x.dtype, x.shape, len(x) / fs))
    print("  peak = %.1f %% of full scale (%.1f dBFS), clipped samples = %d"
          % (100 * peak, 20 * np.log10(peak), clipped))
    if fs < 44100:
        print("  !! sample rate below 44.1 kHz: not marked")
    if clipped:
        print("  !! clipped: re-record with lower input gain")
