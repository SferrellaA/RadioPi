#!/usr/bin/python
'''
Power Spectral Density (PSD) describes the power in a signal over time
Transmission on a frequency will appear as spikes on a curve
'''

# Imports
from helpers import frequency, listen, graphPSD, display
from argparse import ArgumentParser

# Get the frequency to sample
flags = ArgumentParser()
flags.add_argument("-f", "--freq", "--frequency", default="94.5FM")
flags.add_argument("-s", "--sec", "--seconds", default=5, type=int)
demo = flags.parse_args()

# Collect S seconds of sampling on frequency
radioSample = listen(centerFrequency=frequency(demo.freq), sampleLength=demo.sec)

# Generate a PSD visualization from sample
imageFile = graphPSD(
    sample=radioSample, 
    centerFrequency=frequency(demo.freq), 
    title=f"{demo.freq} Capture")

# Display the visualization on onboard inky what
display(imageFile)
