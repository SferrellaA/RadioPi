# Imports
from helpers import frequency, configureRadio, formatSample, audiateCapture
from sys import argv
import asyncio
from time import time
from scipy.signal import decimate, lfilter
from os import system, listdir

# Get the frequency, length to sample
f = "89.7FM"
if len(argv) > 1:
    f = argv[1]
freq = frequency(f)
s = 5
if len(argv) > 2:
    s = int(argv[2])
print(f"Listening on {f} for {s} seconds")

# Configure radio
sampleRate = 1.2e6 
sdr = configureRadio(freq, sampleRate)

# Clear ./raw/ directory of prior samples
system('rm ./raw/*')

# Capture S seconds of audio
async def streaming(start_time, capture_length):
    async for sample in sdr.stream():
        #sample *= np.exp(-1.0j*2.0*np.pi*400000/sampleRate*np.arange(len(sample)))
        sample = formatSample(sample, sampleRate)
        sample.astype("int16").tofile(f"raw/{time()}.raw")

        # this is such a jank way to set a timer
        if time() - start_time  >= capture_length:
            break
    await sdr.stop()
    sdr.close()
asyncio.get_event_loop().run_until_complete(streaming(time(), s))

# Combine multiple .raw captures into one
out = open(f'{f}_capture.raw', 'wb')
for part in listdir('./raw'):
    out.write(open(f'./raw/{part}', 'rb').read())
out.close()

# Play the captured audio
audiateCapture(f"{f}_capture.raw", sampleRate, f"{f}_capture.wav")