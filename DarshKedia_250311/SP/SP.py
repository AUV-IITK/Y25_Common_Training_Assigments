import numpy as np
from scipy.io import wavfile
from scipy import signal
import librosa

audio_data, sr = librosa.load('audio.mpeg', sr=None)

audio_int16 = (audio_data * 32767).astype(np.int16)
wavfile.write('original.wav', sr, audio_int16)

def create_delay(sig, delay_sec, sr):
    delay_samples = int(delay_sec * sr)

    delayed = np.pad(sig, (delay_samples, 0), mode='constant')

    # Trim back to original length
    delayed = delayed[:len(sig)]

    return delayed

signal_0s = create_delay(audio_data, 0, sr)
signal_1s = create_delay(audio_data, 1, sr)
signal_2s = create_delay(audio_data, 2, sr)
signal_3s = create_delay(audio_data, 3, sr)

wavfile.write('delay_0s.wav', sr,
              (signal_0s * 32767).astype(np.int16))

wavfile.write('delay_1s.wav', sr,
              (signal_1s * 32767).astype(np.int16))

wavfile.write('delay_2s.wav', sr,
              (signal_2s * 32767).astype(np.int16))

def normalized_correlation(x, y):

    corr = signal.correlate(x, y, mode='full')

    normalization = np.sqrt(
        np.sum(x**2) * np.sum(y**2)
    )

    corr = corr / normalization

    return corr

def peak_corr_value(corr):
    return np.max(np.abs(corr))

# PART A

reference = signal_1s

corr_0 = normalized_correlation(signal_0s, reference)
corr_1 = normalized_correlation(signal_1s, reference)
corr_2 = normalized_correlation(signal_2s, reference)

print("PART (a)")
print("Correlation (0s vs 1s):", peak_corr_value(corr_0))
print("Correlation (1s vs 1s):", peak_corr_value(corr_1))
print("Correlation (2s vs 1s):", peak_corr_value(corr_2))

# PART B

combined_reference = signal_0s + signal_2s

corr_0c = normalized_correlation(signal_0s, combined_reference)
corr_1c = normalized_correlation(signal_1s, combined_reference)
corr_2c = normalized_correlation(signal_2s, combined_reference)
corr_3c = normalized_correlation(signal_3s, combined_reference)

print("\nPART (b)")
print("Correlation (0s vs combined):", peak_corr_value(corr_0c))
print("Correlation (1s vs combined):", peak_corr_value(corr_1c))
print("Correlation (2s vs combined):", peak_corr_value(corr_2c))
print("Correlation (3s vs combined):", peak_corr_value(corr_3c))