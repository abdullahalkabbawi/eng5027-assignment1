"""Parts 1 and 2: analysis and enhancement of original_speech_5cm.wav and original_speech_1m.wav.

Part 1 (20%) owner: Abdullah. Part 2 (20%) owner: Nommy.
Writes enhanced_speech_5cm.wav and enhanced_speech_1m.wav.

Run: python3 audioplot.py
"""

# ---- Part 1 (Abdullah) ----

import numpy as np                # arrays and maths
import matplotlib.pyplot as plt   # plotting
from scipy.io import wavfile      # WAV reader/writer


def spectrum(x, fs):                                 # one-sided amplitude spectrum in dB
    N = x.size                                       # number of samples in this piece
    X = np.fft.fft(x)                                # N complex DFT coefficients
    amplitude = 2 * np.abs(X) / N                    # amplitude of each frequency
    f = np.arange(N) * fs / N                        # bin k -> k*fs/N Hz
    return f[1:N // 2], 20 * np.log10(amplitude[1:N // 2])   # positive half, skip 0 Hz, in dB


def cut(signal, fs, t0, t1):                         # piece of signal from t0 to t1 seconds
    return signal[int(t0 * fs):int(t1 * fs)]


def plot_recording(filename, name, vowels, s_start, consonants, noise):
    fs, signal = wavfile.read(filename)              # fs = sample rate, signal = samples
    print(name, fs, signal.dtype, signal.shape)      # 48000, int16, (samples,) for mono
    if signal.ndim > 1:                              # stereo file: keep the left channel
        signal = signal[:, 0]
    signal = signal / 32768.0                        # int16 full scale -> -1 to +1
    time = np.arange(signal.size) / fs               # t[n] = n/fs in seconds

    # (i) time domain
    plt.figure()                                     # new figure window
    plt.plot(time, signal)                           # amplitude vs time, linear axes
    plt.xlabel("Time (s)")
    plt.ylabel("Normalised amplitude")
    plt.title(name)
    plt.savefig("time_" + name + ".pdf")             # vector PDF

    # (ii) frequency domain, with (iii)-(v) marked
    f, dB = spectrum(signal, fs)                     # whole recording
    plt.figure()
    plt.plot(f, dB, color="C0")                      # amplitude (dB) vs frequency
    for i, (label, t0, t1, f0) in enumerate(vowels):
        plt.axvline(f0, color="C" + str(i + 1), linestyle="--", label="f0 " + label + " = " + str(f0) + " Hz")
    plt.axvspan(consonants[0], consonants[1], color="orange", alpha=0.2, label="consonants")
    plt.axvspan(noise[0], noise[1], color="grey", alpha=0.3, label="noise only")
    plt.xscale("log")                                # log frequency axis
    plt.xlim(20, fs / 2)                             # audible range up to fs/2
    plt.xlabel("Frequency (Hz)")
    plt.ylabel("Amplitude (dB)")
    plt.title(name)
    plt.legend()
    plt.savefig("frequency_" + name + ".pdf")

    # (iii): each vowel on its own, zoomed to f0 and its first harmonics
    plt.figure()
    for i, (label, t0, t1, f0) in enumerate(vowels):
        f, dB = spectrum(cut(signal, fs, t0, t1), fs)            # spectrum of this vowel only
        plt.plot(f, dB, color="C" + str(i + 1), label=label + " (" + str(t0) + "-" + str(t1) + " s)")
        plt.axvline(f0, color="C" + str(i + 1), linestyle="--")  # your f0 reading
    plt.xlim(50, 1000)                               # linear axis: harmonics f0, 2f0, 3f0 evenly spaced
    plt.xlabel("Frequency (Hz)")
    plt.ylabel("Amplitude (dB)")
    plt.title(name + ": vowels")
    plt.legend()
    plt.savefig("vowels_" + name + ".pdf")

    # (iv) and (v): "s" vs silence, both 0.15 s long
    plt.figure()
    f, dB = spectrum(cut(signal, fs, s_start, s_start + 0.15), fs)
    plt.plot(f, dB, label='"s" (' + str(s_start) + " s)")
    f, dB = spectrum(cut(signal, fs, 0.05, 0.20), fs)            # quiet start, before speaking
    plt.plot(f, dB, label="silence (0.05-0.20 s)")
    plt.xscale("log")
    plt.xlim(20, fs / 2)
    plt.xlabel("Frequency (Hz)")
    plt.ylabel("Amplitude (dB)")
    plt.title(name + ': "s" vs silence')
    plt.legend()
    plt.savefig("s_vs_silence_" + name + ".pdf")


# Sentence: "Paul's father bought six pieces of fresh cheese at the market place."
# vowels = (name, start s, end s, f0 Hz); s_start = the final "s" of "place";
# consonants = (low Hz, high Hz); noise = (low Hz, high Hz)
# All values READ BY EYE from the plots.
plot_recording("original_speech_5cm.wav", "5cm",
               vowels=[("aw in Paul's", 1.10, 1.22, 165), ("ah in father", 1.95, 2.15, 140),
                       ("ee in cheese", 5.78, 5.98, 148), ("ay in place", 9.02, 9.22, 129)],
               s_start=9.30, consonants=(520, 24000), noise=(20, 80))
plot_recording("original_speech_1m.wav", "1m",
               vowels=[("aw in Paul's", 1.08, 1.20, 165), ("ah in father", 1.80, 2.00, 139),
                       ("ee in cheese", 5.92, 6.12, 142), ("ay in place", 9.58, 9.78, 126)],
               s_start=9.86, consonants=(2253, 22000), noise=(22000, 24000))
plt.show()                                           # show all plots

# ---- Part 2 (Nommy) ----