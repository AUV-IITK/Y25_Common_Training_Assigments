import numpy as np
import soundfile as sf
from scipy.io import wavfile
from scipy.signal import correlate

corrupted_wav_path = "audio_file.wav"
true_wav_path = "audio_file_actual.wav"

print("Reading and decoding the underlying MP3 data...")
try:
    data, sample_rate = sf.read(corrupted_wav_path)
    
    sf.write(true_wav_path, data, sample_rate, format='WAV', subtype='PCM_16')
    print(f"-> Successfully created a true WAV file: {true_wav_path}")
except Exception as e:
    print(f"Error decoding the file: {e}")
    exit()


sample_rate, data = wavfile.read(true_wav_path)

#now we have the sound in an array data
data = data.astype(np.float32)

# If the audio is stereo, convert to mono by taking the average of channels
if len(data.shape) > 1:
    data = data.mean(axis=1)

one_sec_samples = sample_rate

# Create zero-padded arrays to keep all signal lengths identical
sig_0s = data.copy()
sig_1s = np.pad(data, (one_sec_samples, 0))[:-one_sec_samples]
sig_2s = np.pad(data, (2 * one_sec_samples, 0))[:-(2 * one_sec_samples)]
sig_3s = np.pad(data, (3 * one_sec_samples, 0))[:-(3 * one_sec_samples)]

# Save the requested files to your disk
wavfile.write("delay_0s.wav", sample_rate, sig_0s.astype(np.int16))
wavfile.write("delay_1s.wav", sample_rate, sig_1s.astype(np.int16))
wavfile.write("delay_2s.wav", sample_rate, sig_2s.astype(np.int16))

print("0s, 1s, and 2s files have been saved successfully.")

print("\n--- Running Part A (Reference = 1s Delay) ---")
ref_A = sig_1s

corr_A_0 = np.max(correlate(sig_0s, ref_A, mode='same'))
corr_A_1 = np.max(correlate(sig_1s, ref_A, mode='same'))
corr_A_2 = np.max(correlate(sig_2s, ref_A, mode='same'))

print(f"Correlation of 0s with 1s Ref: {corr_A_0:.2f}")
print(f"Correlation of 1s with 1s Ref: {corr_A_1:.2f} (Perfect Self-Match)")
print(f"Correlation of 2s with 1s Ref: {corr_A_2:.2f}")

print("\n--- Running Part B (Reference = 0s + 2s Delay) ---")
ref_B = sig_0s + sig_2s

corr_B_0 = np.max(correlate(sig_0s, ref_B, mode='same'))
corr_B_1 = np.max(correlate(sig_1s, ref_B, mode='same'))
corr_B_2 = np.max(correlate(sig_2s, ref_B, mode='same'))
corr_B_3 = np.max(correlate(sig_3s, ref_B, mode='same'))

print(f"Correlation of 0s with Combined Ref: {corr_B_0:.2f}")
print(f"Correlation of 1s with Combined Ref: {corr_B_1:.2f}")
print(f"Correlation of 2s with Combined Ref: {corr_B_2:.2f}")
print(f"Correlation of 3s with Combined Ref: {corr_B_3:.2f}")