#!/usr/bin/python
from helpers import frequency, listen, audiateSample
from sys import argv
from time import time
import matplotlib.pyplot as plt

# Get the frequency to listen on
f = "94.5FM"
if len(argv) > 1:
    f = argv[1]
freq = frequency(f)
print(f"Listenign on {f}")

# Collect radio sample
t = time()
sample = listen(freq, 5)
print(f"Collected {f} sample")

# Graph the sample
plt.specgram(sample, NFFT=2048, Fs=1.2e6)
plt.savefig(f"{t}.png")
plt.close()
print(f"Generated sample visualization ({t}.png)")

'''
# Local FM stations are not consistently tuned within their 200khz band -- an autotuning function is needed
sample *= np.exp(-1.0j*2.0*np.pi*400000/sampleRate*np.arange(len(sample)))
plt.specgram(sample, NFFT=2048, Fs=sampleRate)
plt.savefig(f"adjusted_{t}.png")
'''

# Play sample as audio
print("Playing sample as audio")
audiateSample(sample, f"{f}_sample.wav")
