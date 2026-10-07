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
    print(name, fs, signal.dtype, signal.shape)      # 44100, int16, (samples, 2 channels)
    signal = signal[:, 0] / 32768.0                  # left channel, int16 full scale -> -1 to +1
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

    # (iii) evidence: each vowel on its own, zoomed to f0 and its first harmonics
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

    # (iv) and (v) evidence: an "s" against silence, both 0.06 s long
    plt.figure()
    f, dB = spectrum(cut(signal, fs, s_start, s_start + 0.06), fs)
    plt.plot(f, dB, label='"s" (' + str(s_start) + " s)")
    f, dB = spectrum(cut(signal, fs, 0.05, 0.11), fs)            # quiet start, before speaking
    plt.plot(f, dB, label="silence (0.05-0.11 s)")
    plt.xscale("log")
    plt.xlim(20, fs / 2)
    plt.xlabel("Frequency (Hz)")
    plt.ylabel("Amplitude (dB)")
    plt.title(name + ': "s" vs silence')
    plt.legend()
    plt.savefig("s_vs_silence_" + name + ".pdf")


# Sentence: "I am Abdullah, recording at Glasgow University.
#            We were away a year ago, evaluating pure audio for our DSP lab."
# vowels = (name, start s, end s, f0 Hz); s_start = the "s" in DSP;
# consonants = (low Hz, high Hz); noise = (low Hz, high Hz)
# All values READ BY EYE from the plots (the brief bans automatic detection).
plot_recording("original_speech_5cm.wav", "5cm",
               vowels=[("I", 0.55, 0.75, 136), ("o in Glasgow", 2.28, 2.44, 130),
                       ("au in audio", 5.49, 5.60, 134), ("e in DSP", 6.92, 7.02, 135)],
               s_start=7.05, consonants=(1000, 22050), noise=(20, 80))
plot_recording("original_speech_1m.wav", "1m",
               vowels=[("I", 0.46, 0.64, 132), ("o in Glasgow", 2.18, 2.33, 130),
                       ("au in audio", 5.12, 5.24, 130), ("e in DSP", 6.25, 6.35, 123)],
               s_start=6.38, consonants=(3222, 20060), noise=(20060, 22050))
plt.show()                                           # show all plots

# ---- Part 2 (Nommy) ----