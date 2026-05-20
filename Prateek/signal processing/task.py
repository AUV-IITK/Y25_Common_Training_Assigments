import numpy as np
from scipy.io import wavfile
from scipy.signal import correlate
from pydub import AudioSegment
import os

input_file = "sound file.mpeg" 
wav_file = "converted_audio.wav"

audio = AudioSegment.from_file(input_file)
audio.export(wav_file, format="wav")

fs, data = wavfile.read(wav_file)
if data.ndim > 1:
    data = data.mean(axis=1)

max_delay_s = 3
total_length = len(data) + int(max_delay_s * fs)

def create_delayed_signal(signal, delay_seconds, sample_rate, target_length):
    delay_samples = int(delay_seconds * sample_rate)
    delayed_sig = np.pad(signal, (delay_samples, 0), mode='constant')
    delayed_sig = np.pad(delayed_sig, (0, target_length - len(delayed_sig)), mode='constant')
    return delayed_sig

sig_0s = create_delayed_signal(data, 0, fs, total_length)
sig_1s = create_delayed_signal(data, 1, fs, total_length)
sig_2s = create_delayed_signal(data, 2, fs, total_length)

wavfile.write("delay_0s.wav", fs, sig_0s.astype(np.int16))
wavfile.write("delay_1s.wav", fs, sig_1s.astype(np.int16))
wavfile.write("delay_2s.wav", fs, sig_2s.astype(np.int16))

def get_peak_correlation(sig_a, sig_b):
    corr = correlate(sig_a, sig_b, mode='full', method='fft')
    return np.max(corr)

print("Correlation with 1s Reference")
ref_a = sig_1s
print(f"0s vs 1s ref: {get_peak_correlation(sig_0s, ref_a):.2f}")
print(f"1s vs 1s ref: {get_peak_correlation(sig_1s, ref_a):.2f}")
print(f"2s vs 1s ref: {get_peak_correlation(sig_2s, ref_a):.2f}\n")

print("Correlation with Combined (0s + 2s) Reference")
ref_b = sig_0s + sig_2s
print(f"0s vs New Ref: {get_peak_correlation(sig_0s, ref_b):.2f}")
print(f"1s vs New Ref: {get_peak_correlation(sig_1s, ref_b):.2f}")
print(f"2s vs New Ref: {get_peak_correlation(sig_2s, ref_b):.2f}")
