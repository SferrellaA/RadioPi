# Credits to https://witestlab.poly.edu/blog/capture-and-decode-fm-radio/

# Get the frequency to listen on
from helpers import frequency
from sys import argv
f = "89.7FM"
if len(argv) > 1:
    f = argv[1]
freq = frequency(f)
print(f"Listenign on {f}")

# Configure sample characteristics
sampleRate = 1.2e6 
sampleLength = 2 # seconds
freq = freq - 600000 # determined from manual testing

# Sample the radio
from rtlsdr import RtlSdr
sdr = RtlSdr()
sdr.sample_rate = sampleRate
sdr.center_freq = freq
sdr.gain = 'auto'
sample = sdr.read_samples(sampleRate * sampleLength)
sdr.close()

# Prepare to do maths
import numpy as np
from scipy.signal import decimate, lfilter

# Convert sample to a numpy array
sample = np.array(sample).astype("complex64")

# Narrow sample to the single station
# fm broadcasts use 200khz (200e3) bandwidth
sample = decimate(sample, int(sampleRate / 200e3))
sampleRate = float(200e3)

# "demodulate with a polar discriminator"
# I still need to learn what that means
sample = np.angle(sample[1:] * np.conj(sample[:-1]))

# De-emphasis the sample 
# Americas use 75 µs
x = np.exp(-1/(sampleRate * 75e-6)) 
sample = lfilter([1-x], [1,-x], sample)

# Narrow down to just monoaudio part of fm broadcast
sample = decimate(sample, int(sampleRate/44100.0))

# Write to raw file
sample *= 30000 / np.max(np.abs(sample)) # to adjust volume
sample.astype("int16").tofile("file.raw")

# Convert to, play .wav audio file
from os import system as exec
exec(f'ffmpeg -hide_banner -loglevel error -y -f s16le -r {sampleRate} -i file.raw file.wav')
exec('cvlc --quiet --play-and-exit file.wav')