from sys import argv
from os import system as exec
from helpers import *

# Select the frequency
f = "89.7FM"
if len(argv) > 1:
    f = argv[1]
freq = frequency(f)
print(f"Listenign on {f}")

# The demo
#sample = listen(freq, byteCount=1024e3, sampleRate=2e6)
import asyncio


async def streaming(freq):
    from rtlsdr import RtlSdr
    sdr = RtlSdr()
    sdr.sample_rate = 1e6
    sdr.center_freq = freq
    sdr.gain = 'auto'

    # gotta figure out what/how the async library works
    # need to save samples as they are collected if you want to do this on a pi

    async for samples in sdr.stream():
        print(len(samples))
    await sdr.stop()
    sdr.close()

loop = asyncio.get_event_loop()
loop.run_until_complete(streaming(freq))

exit()


import numpy as np
x7 = np.array(sample).astype("complex64")

# need to sample down to first the actual 200khz broadcast, and then the audio part

x7 *= 10000 / np.max(np.abs(x7)) # to adjust volume
x7.astype("int16").tofile("file.raw")
#exec('ffmpeg -y -f s16le -r 45600 -i file.raw file.wav')

# https://witestlab.poly.edu/blog/capture-and-decode-fm-radio/