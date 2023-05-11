#!/usr/bin/python
from helpers import frequency, audiateCapture, sampleAudio
from sys import argv

# Get the frequency, length to sample
f = "94.5FM"
if len(argv) > 1:
    f = argv[1]
freq = frequency(f)
s = 5
if len(argv) > 2:
    s = int(argv[2])

# Capture S seconds of audio
print(f"Sampling on {f} for {s} seconds")
sampleAudio(freq, s, outFile=f"{f}_capture.raw")

# Play the captured audio
print(f"Playing {f}_capture.wav")
audiateCapture(f"{f}_capture.raw", f"{f}_capture.wav")