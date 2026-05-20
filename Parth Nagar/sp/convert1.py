import numpy as np
import scipy.io.wavfile as wavfile
from pydub import AudioSegment

audio = AudioSegment.from_mp3("AUDIO-2026-05-17-14-20-50.mp3")
audio.export("output.wav", format="wav")
fs, data = wavfile.read("output.wav")
data = data.astype(np.float64)
if data.ndim == 2:
    data = data.mean(axis=1)
n_zeros    = 1 * fs
silence    = np.zeros(n_zeros)
delayed_1s = np.concatenate([silence, data])
n_zeros_2  = 2 * fs
delayed_2s = np.concatenate([np.zeros(n_zeros_2), data])
n_zeros_3  = 3 * fs
delayed_3s = np.concatenate([np.zeros(n_zeros_3), data])
def save_wav(filename, signal, sample_rate):
    clipped = np.clip(signal, -32768, 32767).astype(np.int16)
    wavfile.write(filename, sample_rate, clipped)

save_wav("signal_0s.wav", data,       fs)
save_wav("signal_1s.wav", delayed_1s, fs)
save_wav("signal_2s.wav", delayed_2s, fs)
save_wav("signal_3s.wav", delayed_3s, fs)
print("All WAV files saved!")
def peak_correlation(sig_a, sig_b):
    N = max(len(sig_a), len(sig_b))
    a = np.pad(sig_a, (0, N - len(sig_a)))
    b = np.pad(sig_b, (0, N - len(sig_b)))
    rms_a = np.sqrt(np.mean(a**2))
    rms_b = np.sqrt(np.mean(b**2))
    if rms_a == 0 or rms_b == 0:
        return 0.0
    a /= rms_a
    b /= rms_b
    fa   = np.fft.rfft(a, n=2*N)
    fb   = np.fft.rfft(b, n=2*N)
    corr = np.fft.irfft(fa * np.conj(fb))
    return float(np.max(np.abs(corr)) / N)
reference_a = delayed_1s
print("\nPart a) Reference = 1s delay signal")
print(f"  0s delay vs 1s ref : {peak_correlation(data,       reference_a):.6f}")
print(f"  1s delay vs 1s ref : {peak_correlation(delayed_1s, reference_a):.6f}")
print(f"  2s delay vs 1s ref : {peak_correlation(delayed_2s, reference_a):.6f}")
len_max       = max(len(data), len(delayed_2s))
sig0_pad      = np.pad(data,       (0, len_max - len(data)))
sig2_pad      = np.pad(delayed_2s, (0, len_max - len(delayed_2s)))
new_reference = sig0_pad + sig2_pad
save_wav("signal_new_ref.wav", new_reference, fs)
print("\nPart b) New Reference = 0s + 2s combined")
print(f"  0s delay vs new ref : {peak_correlation(data,       new_reference):.6f}")
print(f"  1s delay vs new ref : {peak_correlation(delayed_1s, new_reference):.6f}")
print(f"  2s delay vs new ref : {peak_correlation(delayed_2s, new_reference):.6f}")
print(f"  3s delay vs new ref : {peak_correlation(delayed_3s, new_reference):.6f}")