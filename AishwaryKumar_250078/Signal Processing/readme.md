Output :-
Part A: Reference (1s Delay)
Correlation of 0s with 1s reference: -0.0054
Correlation of 1s with 1s reference: 1.0000
Correlation of 2s with 1s reference: -0.0046

Part B: New Reference (0s + 2s)
Correlation of 0s with New Reference: 0.6709
Correlation of 1s with New Reference: -0.0068
Correlation of 2s with New Reference: 0.6597
Correlation of 3s with New Reference: -0.0071

Code :-

import numpy as np
from pydub import AudioSegment

audio = AudioSegment.from_file("pikachu.wav")
audio = audio.set_channels(1)  # Convert to mono for easier correlation math

def create_delayed_version(delay_sec):
    # Create silence for the delay
    silence = AudioSegment.silent(duration=delay_sec * 1000)
    delayed_audio = silence + audio
    filename = f"delayed_{delay_sec}s.wav"
    delayed_audio.export(filename, format="wav")
    return np.array(delayed_audio.get_array_of_samples())

# Generate signals
sig_0s = create_delayed_version(0)
sig_1s = create_delayed_version(1)
sig_2s = create_delayed_version(2)
sig_3s = create_delayed_version(3) # Needed for part B

def get_correlation(sig1, sig2):
    # Ensure signals are the same length for direct comparison
    n = max(len(sig1), len(sig2))
    s1 = np.pad(sig1, (0, n - len(sig1)))
    s2 = np.pad(sig2, (0, n - len(sig2)))
    corr = np.corrcoef(s1, s2)[0, 1]
    return corr

# Part A: Reference is 1s delay
print("Part A: Reference (1s Delay)")
ref_a = sig_1s
for label, sig in [("0s", sig_0s), ("1s", sig_1s), ("2s", sig_2s)]:
    val = get_correlation(ref_a, sig)
    print(f"Correlation of {label} with 1s reference: {val:.4f}")

# Part B: New Reference (0s + 2s)
print("\nPart B: New Reference (0s + 2s)")

sig_0s_padded = np.pad(sig_0s, (0, len(sig_2s) - len(sig_0s)))
new_ref = sig_0s_padded + sig_2s

for label, sig in [("0s", sig_0s), ("1s", sig_1s), ("2s", sig_2s), ("3s", sig_3s)]:
    val = get_correlation(new_ref, sig)
    print(f"Correlation of {label} with New Reference: {val:.4f}")

Logic of code :-
I have loaded the given audio file for processing using AudioSegment.
Next is the function for creating delayed audio, in which I add silence of required delay seconds
Then there is correlation function, in which
    i) used padding to match the arrays length.
    ii) used np.corrcoef to correlation coefficient which returns a value between -1 and 1 depending on the matching of two audio signals
Then there is comparison taking 1s delayed audio referrence
then the referrence has been changed to sum of 0s and 2s delayed audio.
And finally the correalation values have been printed
