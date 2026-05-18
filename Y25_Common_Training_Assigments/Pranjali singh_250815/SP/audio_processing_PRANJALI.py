import numpy as np
import soundfile as sf
import librosa
from scipy.signal import correlate

print("Reading and converting audio file...")

data, sample_rate = librosa.load('AUDIO-2026-05-18-05-21-06.mp3', sr=None, mono=True)


def create_delay(signal, seconds, sr):
    padding = int(seconds * sr)
    return np.concatenate((np.zeros(padding), signal))


sig_0s = create_delay(data, 0, sample_rate)
sig_1s = create_delay(data, 1, sample_rate)
sig_2s = create_delay(data, 2, sample_rate)
sig_3s = create_delay(data, 3, sample_rate) 


max_len = len(sig_3s)
sig_0s = np.pad(sig_0s, (0, max_len - len(sig_0s)))
sig_1s = np.pad(sig_1s, (0, max_len - len(sig_1s)))
sig_2s = np.pad(sig_2s, (0, max_len - len(sig_2s)))


sf.write('delay_0s.wav', sig_0s, sample_rate)
sf.write('delay_1s.wav', sig_1s, sample_rate)
sf.write('delay_2s.wav', sig_2s, sample_rate)
print("Successfully created: delay_0s.wav, delay_1s.wav, delay_2s.wav\n")


def get_peak_correlation(sig1, sig2):
    corr = correlate(sig1, sig2, mode='same')
    return np.max(corr)


ref_A = sig_1s
print("=== PART A RESULTS (Ref: 1s Delay) ===")
print(f"0s Signal vs 1s Ref: {get_peak_correlation(sig_0s, ref_A):.4f}")
print(f"1s Signal vs 1s Ref: {get_peak_correlation(sig_1s, ref_A):.4f}")
print(f"2s Signal vs 1s Ref: {get_peak_correlation(sig_2s, ref_A):.4f}\n")


ref_B = sig_0s + sig_2s
print("=== PART B RESULTS (Ref: 0s + 2s Combined) ===")
print(f"0s Signal vs Combined Ref: {get_peak_correlation(sig_0s, ref_B):.4f}")
print(f"1s Signal vs Combined Ref: {get_peak_correlation(sig_1s, ref_B):.4f}")
print(f"2s Signal vs Combined Ref: {get_peak_correlation(sig_2s, ref_B):.4f}")
print(f"3s Signal vs Combined Ref: {get_peak_correlation(sig_3s, ref_B):.4f}")