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

# Sample the radio
from rtlsdr import RtlSdr
sdr = RtlSdr()
sdr.sample_rate = sampleRate
sdr.center_freq = freq
sdr.gain = 'auto'
sample = sdr.read_samples(sampleRate * 2) # 2 seconds
sdr.close()

# Prepare to do maths
import numpy as np
sample = np.array(sample) #.astype("complex64")

from time import time
import matplotlib.pyplot as plt
plt.specgram(sample, NFFT=2048, Fs=sampleRate)
plt.savefig(f"raw_{time()}.png")

'''
I'm testing this with 90.1, which transmits correctly
But 89.7 is shifted a bit
'''
#sample *= np.exp(-1.0j*2.0*np.pi*400000/sampleRate*np.arange(len(sample)))
plt.specgram(sample, NFFT=2048, Fs=sampleRate)
plt.savefig(f"mod_{time()}.png")

plt.close()

def audiate(sample, sampleRate):
    from scipy.signal import decimate, lfilter

    sample = decimate(sample, int(sampleRate / 200e3))
    sampleRate = float(200e3)
    sample = np.angle(sample[1:] * np.conj(sample[:-1]))
    x = np.exp(-1/(sampleRate * 75e-6)) 
    sample = lfilter([1-x], [1,-x], sample)
    sample = decimate(sample, int(sampleRate/44100.0))
    sample *= 30000 / np.max(np.abs(sample))
    
    from os import system
    system('rm sample.raw')
    sample.astype("int16").tofile(f"sample.raw")
    system(f'ffmpeg -hide_banner -loglevel error -y -f s16le -r {sampleRate} -i sample.raw sample.wav')
    system('cvlc --quiet --play-and-exit sample.wav')

audiate(sample, sampleRate)

