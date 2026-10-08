import numpy as np
from scipy.signal import butter, sosfilt
from matplotlib import pyplot as plt 
from scipy.io import wavfile

fs, signal = wavfile.read('original_speech_5cm.wav')
import numpy as np

#Stereo to mono conversion
if signal.ndim > 1:
        signal = np.mean(signal, axis=1) 
        signal = signal.astype(float)

# def bandpass_filter(signal, fs, lowcut, highcut, num_taps=101):

    # Time indices centred around zero
#    n = np.arange(num_taps) - (num_taps - 1) / 2

    # Ideal band-pass impulse response
#    h = (
#        2 * highcut / fs * np.sinc(2 * highcut * n / fs)
#        - 2 * lowcut / fs * np.sinc(2 * lowcut * n / fs)
#    )

    # Hann window
#    window = np.hanning(num_taps)

    # Apply window
#    h *= window

    # Filter the signal
#    return np.convolve(signal, h, mode="same")

def bandpass_filter(signal, lowcut, highcut, fs):
    sos = butter(
        4,
        [lowcut, highcut],
        btype="bandpass",
        fs=fs,
        output="sos"
    )
    return sosfilt(sos, signal)


def apply_drive(signal, drive):
    return signal * drive

def nonlinear_process(signal):
    return np.tanh(signal)

def apply_wet_gain(signal, wet):
    return signal * wet

def mix_signals(original, processed):
    return original + processed

def aural_exciter(audio, fs, lowcut=2000, highcut=12000, drive=3.0, wet=0.2):

    band = bandpass_filter( audio, lowcut, highcut, fs)
    driven = apply_drive(band, drive)
    excited = nonlinear_process(driven)
    excited_new = apply_wet_gain(excited, wet)
    output = mix_signals(audio, excited_new)

    return output

output = aural_exciter(signal, fs)

def plot_spectrum(original, output, fs):

    N = signal.size
    time = np.arange(N) / fs

    # Frequency axis
    frequencies = np.fft.rfftfreq(N, 1 / fs)

    # FFT of original and processed signals
    original_fft = np.fft.rfft(original)
    output_fft = np.fft.rfft(output)

    # Magnitude
    original_mag = np.abs(original_fft)
    output_mag = np.abs(output_fft)

    # Plot
    plt.figure(figsize=(10, 5))

    plt.plot(
        frequencies,
        original_mag,
        label="Original",
        alpha=0.7
    )

    plt.plot(
        frequencies,
        output_mag,
        label="Aural Exciter",
        alpha=0.7
    )

    plt.xlabel("Frequency (Hz)")
    plt.ylabel("Magnitude")
    plt.title("Frequency Spectrum: Original vs Aural Exciter")

    plt.xlim(0, 20000)

    plt.legend()
    plt.grid(True)
    plt.show()
plot_spectrum(signal, output, fs)

 