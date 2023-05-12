#!/usr/bin/python
'''
FM radio stations broadcast within a 200khz band of radio spectrum

but

The local FM stations where I live are not consistently tuned, with
some stations broadcasting at offsets. This isn't a problem when
tuning a radio with physical knobs, but a digital radio will only 
collect exactly what you tell it to. Being able to see if the SDR
is tuned correctly requires trial-and-error, which this test file 
aims to help with.
'''

# Imports
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

# Play sample as audio
print("Playing sample as audio")
audiateSample(sample, f"{f}_sample.wav")
