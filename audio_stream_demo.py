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


# async sample
import asyncio
from rtlsdr import RtlSdr
import numpy as np


sdr = RtlSdr()
sdr.sample_rate = sampleRate
sdr.center_freq = freq
sdr.gain = 'auto'




from time import time
from scipy.signal import decimate, lfilter

'''
async def streaming():
    async for sample in sdr.stream():
        sample = decimate(sample, 6)
        sample = np.angle(sample[1:] * np.conj(sample[:-1]))
        # de-emphasis the sample
        sample = decimate(sample, int(sampleRate/44100.0))
        sample *= 30000 / np.max(np.abs(sample))
        sample.astype("int16").tofile(f"raw/{time()}.raw")
    await sdr.stop()
    print("stopping")
    sdr.close()

asyncio.get_event_loop().run_until_complete(streaming())

'''
sampleRate = float(200e3)
async def streaming(start_time, capture_length):
    async for sample in sdr.stream():
        #sample *= np.exp(-1.0j*2.0*np.pi*400000/sampleRate*np.arange(len(sample)))
        sample = decimate(sample, 6)
        sample = np.angle(sample[1:] * np.conj(sample[:-1]))
        x = np.exp(-1/(sampleRate * 75e-6)) 
        sample = lfilter([1-x], [1,-x], sample)
        sample = decimate(sample, int(sampleRate/44100.0))
        sample *= 30000 / np.max(np.abs(sample))
        sample.astype("int16").tofile(f"raw/{time()}.raw")

        # this is such a jank way to set a timer
        if time() - start_time  >= capture_length:
            break
    await sdr.stop()
    sdr.close()

from os import system
system('rm ./raw/*')

asyncio.get_event_loop().run_until_complete(streaming(time(), 5))

from os import listdir
out = open('file.raw', 'wb')
for part in listdir('./raw'):
    out.write(open(f'./raw/{part}', 'rb').read())
out.close()
system(f'ffmpeg -hide_banner -loglevel error -y -f s16le -r {sampleRate} -i file.raw file.wav')
system('cvlc --quiet --play-and-exit file.wav')