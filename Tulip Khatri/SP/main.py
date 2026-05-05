import numpy as np 
from scipy.io import wavfile
from scipy import signal 
import librosa 

audio_data,sr= librosa.load('audio.mpeg',sr=None)
audio_int16 = (audio_data * 32767).astype(np.int16)
wavfile.write('original.wav', sr, audio_int16)

def create_delay(sig,delay_sec,sr):
    delay_samples = int(delay_sec * sr)
    return np.pad(sig, (delay_samples, 0), mode='constant')    

signal_0s = audio_data
signal_1s = create_delay(audio_data, 1, sr)
signal_2s = create_delay(audio_data, 2, sr)
signal_3s = create_delay(audio_data, 3, sr)

def normalized_corr(x, y):
    corr = signal.correlate(x, y, mode='full')
    norm = np.sqrt(np.sum(x**2) * np.sum(y**2))
    return corr / norm

def get_peak_lag(corr, x, y, sr):
    lags = np.arange(-len(y)+1, len(x))
    peak_index = np.argmax(corr)
    return lags[peak_index] / sr

ref = signal_1s

corr_0 = normalized_corr(signal_0s, ref)
corr_1 = normalized_corr(signal_1s, ref)
corr_2 = normalized_corr(signal_2s, ref)

print("0s vs 1s delay:", get_peak_lag(corr_0, signal_0s, ref, sr))
print("1s vs 1s delay:", get_peak_lag(corr_1, signal_1s, ref, sr))
print("2s vs 1s delay:", get_peak_lag(corr_2, signal_2s, ref, sr))

def make_same_length(a, b):
    max_len = max(len(a), len(b))
    a = np.pad(a, (0, max_len - len(a)))
    b = np.pad(b, (0, max_len - len(b)))
    return a, b

signal_0s, signal_2s = make_same_length(signal_0s, signal_2s)
combined = signal_0s + signal_2s

corr_0c = normalized_corr(signal_0s, combined)
corr_1c = normalized_corr(signal_1s, combined)
corr_2c = normalized_corr(signal_2s, combined)
corr_3c = normalized_corr(signal_3s, combined)

print("0s vs combined:", get_peak_lag(corr_0c, signal_0s, combined, sr))
print("1s vs combined:", get_peak_lag(corr_1c, signal_1s, combined, sr))
print("2s vs combined:", get_peak_lag(corr_2c, signal_2s, combined, sr))
print("3s vs combined:", get_peak_lag(corr_3c, signal_3s, combined, sr))


