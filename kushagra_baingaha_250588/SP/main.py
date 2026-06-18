import numpy as np
from scipy.io import wavfile
from scipy.signal import correlate
import matplotlib.pyplot as plt

sample_rate, audio = wavfile.read("audio.wav")
samples_one_second=sample_rate
mono = audio.mean(axis=1).astype(np.float64)

print(mono.shape)
silence_1  = np.zeros(samples_one_second, dtype=np.int16)
silence_2=np.zeros(samples_one_second*2, dtype=np.int16)
silence_3=np.zeros(samples_one_second*3, dtype=np.int16)

delayed_1 = np.concatenate([silence_1, mono])
delayed_2 = np.concatenate([silence_2, mono])
delayed_3 = np.concatenate([silence_3, mono])

wavfile.write('audio_delayed_1.wav', sample_rate, delayed_1.astype(np.int16))
wavfile.write('audio_delayed_2.wav', sample_rate, delayed_2.astype(np.int16))


signals=[mono,delayed_1,delayed_2,delayed_3]
value_1=[]

for d in [0, 1, 2]:
    sig = signals[d]
    max_len = max(len(sig), len(delayed_1))
    s = np.pad(sig, (0, max_len - len(sig)))
    r = np.pad(delayed_1, (0, max_len - len(delayed_1)))

    corr  = correlate(s, r, mode="full")
    value_1.append(np.max(np.abs(corr)))

max_len_02 = max(len(signals[0]), len(signals[2]))
s0 = np.pad(signals[0], (0, max_len_02 - len(signals[0])))
s2 = np.pad(signals[2], (0, max_len_02 - len(signals[2])))

new_ref=s0+s2

value_2=[]
for d in [0, 1, 2, 3]:
    sig = signals[d]
    max_len = max(len(sig), len(new_ref))
    s = np.pad(sig, (0, max_len - len(sig)))
    r = np.pad(new_ref, (0, max_len - len(new_ref)))

    corr  = correlate(s, r, mode="full")
    value_2.append(np.max(np.abs(corr)))

print(f'value_1:{value_1} value_2: {value_2}')

