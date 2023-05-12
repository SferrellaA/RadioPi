#!/usr/bin/python
'''
Capture an FM broadcast and listen to it's audio!
'''

# Imports
from helpers import frequency, audiateCapture, sampleAudio
from argparse import ArgumentParser

# Get the frequency, length to sample
flags = ArgumentParser()
flags.add_argument("-f", "--freq", "--frequency", default="94.5FM")
flags.add_argument("-s", "--sec", "--seconds", default=5, type=int)
demo = flags.parse_args()

# Write what files to store sample, audio to
sampleFile = f"{demo.freq}_capture.raw"
audioFile = f"{demo.freq}_capture.wav"

# Capture some seconds of audio
print(f"Sampling on {demo.freq} for {demo.sec} seconds")
sampleAudio(centerFrequency=frequency(demo.freq), sampleLength=demo.sec, outFile=sampleFile)

# Play the captured audio
print(f"Playing {audioFile}")
audiateCapture(rawFile=sampleFile, audioName=audioFile)