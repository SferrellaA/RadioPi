# Credits to https://witestlab.poly.edu/blog/capture-and-decode-fm-radio/

# Imports
from helpers import frequency, audiateSample
from sys import argv
from rtlsdr import RtlSdr
import numpy as np
from time import time
import matplotlib.pyplot as plt

# Get the frequency to listen on
f = "89.7FM"
if len(argv) > 1:
    f = argv[1]
freq = frequency(f)
print(f"Listenign on {f}")

# Configure radio
sampleRate = 1.2e6 
sdr = RtlSdr()
sdr.sample_rate = sampleRate
sdr.center_freq = freq
sdr.gain = 'auto'

# Collect radio sample
t = time()
sample = np.array(sdr.read_samples(sampleRate * 2)) # 2 seconds
sdr.close()
print(f"Collected {f} sample")

# Graph the sample
plt.specgram(sample, NFFT=2048, Fs=sampleRate)
plt.savefig(f"{t}.png")
print(f"Generated sample visualization ({t}.png)")

'''
# Local FM stations are not consistently tuned within their 200khz band -- an autotuning function is needed
sample *= np.exp(-1.0j*2.0*np.pi*400000/sampleRate*np.arange(len(sample)))
plt.specgram(sample, NFFT=2048, Fs=sampleRate)
plt.savefig(f"adjusted_{t}.png")
'''

plt.close()

# Play sample as audio
print("Playing sample as audio")
audiateSample(sample, sampleRate, f"{f}_sample.wav")
