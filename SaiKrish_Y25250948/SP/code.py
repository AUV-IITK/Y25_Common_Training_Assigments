import librosa
import numpy as np
import soundfile as sf
from scipy.signal import correlate

input_file = "pikachu.mpeg"

data, fs = librosa.load(input_file, sr=None)

max_delay = 3
total_length = len(data) + int(max_delay * fs)

def create_delayed_signal(signal, delay_seconds, sample_rate, target_length):

    delay_samples = int(delay_seconds * sample_rate)

    delayed_sig = np.pad(signal, (delay_samples, 0), mode='constant')

    delayed_sig = np.pad(
        delayed_sig,
        (0, target_length - len(delayed_sig)),
        mode='constant'
    )

    return delayed_sig

sig_0s = create_delayed_signal(data, 0, fs, total_length)
sig_1s = create_delayed_signal(data, 1, fs, total_length)
sig_2s = create_delayed_signal(data, 2, fs, total_length)
sig_3s = create_delayed_signal(data, 3, fs, total_length)

sf.write("delay_0s.wav", sig_0s, fs)
sf.write("delay_1s.wav", sig_1s, fs)
sf.write("delay_2s.wav", sig_2s, fs)

def get_correlation(sig_a, sig_b):

    corr = correlate(sig_a, sig_b, mode='valid')

    return corr[0]

print("PART A")

print(f"Correlation between 0s and 1s: {get_correlation(sig_0s, sig_1s):.2f}")
print(f"Correlation between 1s and 1s: {get_correlation(sig_1s, sig_1s):.2f}")
print(f"Correlation between 2s and 1s: {get_correlation(sig_2s, sig_1s):.2f}")

print("\nPART B")

new_ref = sig_0s + sig_2s

print(f"Correlation between 0s and New: {get_correlation(sig_0s, new_ref):.2f}")
print(f"Correlation between 1s and New: {get_correlation(sig_1s, new_ref):.2f}")
print(f"Correlation between 2s and New: {get_correlation(sig_2s, new_ref):.2f}")
print(f"Correlation between 3s and New: {get_correlation(sig_3s, new_ref):.2f}")