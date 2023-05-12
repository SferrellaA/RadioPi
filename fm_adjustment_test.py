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
import matplotlib.pyplot as plt
from argparse import ArgumentParser

# Get the frequency, length to sample
flags = ArgumentParser()
flags.add_argument("-f", "--freq", "--frequency", default="94.5FM")
flags.add_argument("-s", "--sec", "--seconds", default=5, type=int)
demo = flags.parse_args()

# Collect radio sample
sample = listen(centerFrequency=frequency(demo.freq), sampleLength=demo.sec)
print(f"Collected {demo.freq} sample")

# Graph the sample
plt.specgram(sample, NFFT=2048, Fs=1.2e6)
plt.savefig(f"{demo.freq}.png")
plt.close()
print(f"Generated sample visualization ({demo.freq}.png)")

# Play sample as audio
print("Playing sample as audio")
audiateSample(sample, f"{demo.freq}_sample.wav")
