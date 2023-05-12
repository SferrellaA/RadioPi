#!/usr/bin/python
'''
Capture an FM broadcast and listen to it's audio!
'''

# Imports
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

# Write what files to store sample, audio to
sampleFile = f"{f}_capture.raw"
audioFile = f"{f}_capture.wav"

# Capture S seconds of audio
print(f"Sampling on {f} for {s} seconds")
sampleAudio(centerFrequency=freq, sampleLength=s, outFile=sampleFile)

# Play the captured audio
print(f"Playing {audioFile}")
audiateCapture(rawFile=sampleFile, audioName=audioFile)