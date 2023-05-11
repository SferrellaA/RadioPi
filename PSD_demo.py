#!/usr/bin/python
'''
Power Spectral Density (PSD) describes the power in a signal over time
Transmission on a frequency will appear as spikes on a curve
'''

# Imports
from sys import argv
from helpers import frequency, listen, graphPSD, display

# Select the frequency
f = "433.3mhz"
if len(argv) > 1:
    f = argv[1]
freq = frequency(f)
print(f"Listening on {f}")

# Collect S seconds of sampling on frequency
radioSample = listen(centerFrequency=freq, sampleLength=5)

# Generate a PSD visualization from sample
imageFile = graphPSD(
    sample=radioSample, 
    centerFrequency=freq, 
    title=f"{f} Capture")

# Display the visualization on onboard inky what
display(imageFile)
