import librosa
import soundfile as sf
import numpy as np

input_file = "sound file.mpeg"

signal, sr = librosa.load(input_file, sr=None)

def create_delay(signal, sr, delay_sec):

    delay_samples = int(delay_sec * sr)

    delayed_signal = np.concatenate(
        (np.zeros(delay_samples), signal)
    )

    return delayed_signal

delay0 = create_delay(signal, sr, 0)
delay1 = create_delay(signal, sr, 1)
delay2 = create_delay(signal, sr, 2)
delay3 = create_delay(signal, sr, 3)

sf.write("delay0s.wav", delay0, sr)
sf.write("delay1s.wav", delay1, sr)
sf.write("delay2s.wav", delay2, sr)
sf.write("delay3s.wav", delay3, sr)

def docorrelation(sig1, sig2):

    min_len = min(len(sig1), len(sig2))

    sig1 = sig1[:min_len]
    sig2 = sig2[:min_len]

    corr = np.correlate(sig1, sig2)

    return corr[0]

ref_signal = delay1

corr_0 = docorrelation(delay0, ref_signal)
corr_1 = docorrelation(delay1, ref_signal)
corr_2 = docorrelation(delay2, ref_signal)
print(f"Correlation (0s,1s): {corr_0}")
print(f"Correlation (1s,1s): {corr_1}")
print(f"Correlation (2s,1s): {corr_2}")

max_len = max(len(delay0), len(delay2))

sig0 = np.pad(delay0, (0, max_len - len(delay0)))
sig2 = np.pad(delay2, (0, max_len - len(delay2)))

new_reference = sig0 + sig2

corr0new = docorrelation(delay0, new_reference)
corr1new = docorrelation(delay1, new_reference)
corr2new = docorrelation(delay2, new_reference)
corr3new = docorrelation(delay3, new_reference)

print(f"Correlation (0s,new ref): {corr0new}")
print(f"Correlation (1s,new ref): {corr1new}")
print(f"Correlation (2s,new ref): {corr2new}")
print(f"Correlation (3s,new ref): {corr3new}")