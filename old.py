from rtlsdr import RtlSdr

sdr = RtlSdr()
sdr.sample_rate = 1.2e6
sdr.center_freq = 433.3e6 #89.7 FM, 88.5 FM
sdr.gain = 'auto'

capture = sdr.read_bytes(1024*128)
sdr.close()

print('---[{}]---'.format(len(capture)))

import matplotlib.pyplot as plt

plt.figure(num=None, figsize=(4.3,3.2)) # screen is 3.33x2.5 inches, 400x300 pixels
plt.psd(x=capture, 
        NFFT=1024, 
        Fs=sdr.sample_rate/1e6, 
        Fc=sdr.center_freq/1e6, 
        color='red', 
        )
plt.xlabel("Frequency (MHz)") 
plt.ylabel("Relative power (db)")
plt.savefig('capture.png', bbox_inches='tight') #, pad_inches=0)

print('---[capture.png]---')

from inky.auto import auto
from PIL import Image

display = auto()
img = Image.open('capture.png').convert('RGB')

pixels = img.load()
for x in range(img.size[0]):
    for y in range(img.size[1]):
        if pixels[x,y] == (255,255,255): #leave the white background alone
            continue
        elif pixels[x,y] == (255,0,0): #leave the center of the red line alone
            continue
        else:
            pixels[x,y] = (0,0,0) #make every other pixel black
img = img.convert('P', palette=Image.ADAPTIVE)#, colors=3)
img.save('display.png')
img = img.transpose(Image.FLIP_TOP_BOTTOM) #just because of how the screen sits on my desk
img = img.transpose(Image.FLIP_LEFT_RIGHT)
#img = img.resize(display.resolution)
display.set_image(img)
display.show()

print('---[display]---')