import numpy as np
import soundfile as sf
from scipy.signal import correlate

# =============================
# STEP 1: Load Original Audio
# =============================
audio, sr = sf.read("input.wav")   # Replace with your file name

# If stereo, convert to mono
if len(audio.shape) > 1:
    audio = np.mean(audio, axis=1)

print("Sample Rate:", sr)

# =============================
# STEP 2: Function to Add Delay
# =============================
def add_delay(signal, delay_sec, sr):
    delay_samples = int(delay_sec * sr)
    delayed = np.concatenate((np.zeros(delay_samples), signal))
    return delayed

# =============================
# STEP 3: Create Delayed Signals
# =============================
sig0 = add_delay(audio, 0, sr)
sig1 = add_delay(audio, 1, sr)
sig2 = add_delay(audio, 2, sr)
sig3 = add_delay(audio, 3, sr)

# Save files
sf.write("delay_0s.wav", sig0, sr)
sf.write("delay_1s.wav", sig1, sr)
sf.write("delay_2s.wav", sig2, sr)
sf.write("delay_3s.wav", sig3, sr)

print("Delayed files saved!")

# =============================
# STEP 4: Correlation Function
# =============================
def corr_value(x, y):
    corr = correlate(x, y, mode='full')
    return np.max(corr)

# Make same length helper
def same_length(a, b):
    max_len = max(len(a), len(b))
    a = np.pad(a, (0, max_len-len(a)))
    b = np.pad(b, (0, max_len-len(b)))
    return a, b

# =============================
# PART A
# Reference = 1s delay
# =============================
print("\nPART A Correlations (Reference = 1s):")

for name, sig in [("0s", sig0), ("1s", sig1), ("2s", sig2)]:
    x, y = same_length(sig, sig1)
    val = corr_value(x, y)
    print(f"Correlation {name} with 1s = {val}")

# =============================
# PART B
# New Reference = 0s + 2s
# =============================
sig0_p, sig2_p = same_length(sig0, sig2)
new_ref = sig0_p + sig2_p

sf.write("new_reference.wav", new_ref, sr)

print("\nPART B Correlations (Reference = 0s + 2s):")

for name, sig in [("0s", sig0), ("1s", sig1), ("2s", sig2), ("3s", sig3)]:
    x, y = same_length(sig, new_ref)
    val = corr_value(x, y)
    print(f"Correlation {name} with new_ref = {val}")