def frequency(shortHand):
    freq = 1
    def parser(mod, list):
        for x in list:
            nonlocal shortHand
            if shortHand.endswith(x):
                nonlocal freq
                freq = mod
                shortHand = shortHand.replace(x, "")
    try:
        parser(1e3, ["KHZ", "Khz", "khz"])
        parser(1e6, ["MHZ", "MHz", "Mhz", "mhz", "FM", "Fm", "fm", "VHF", "vhf"])
        parser(1e9, ["GHZ", "GHz", "Ghz", "ghz"])
        parser(1, ["HZ", "hz", "htz"])
        parser(0, ["AM", "am"]) # not sure how AM works
    except:
        pass
    try:
        freq *= float(shortHand)
    except:
        exit("Invalid frequency")
    return freq

from PIL import Image
def colorCorrect(img: Image):
    pixels = img.load()
    for x in range(img.size[0]):
        for y in range(img.size[1]):
            # arbitrary color cutoffs
            # red and black must be swapped b/c???
            r, g, b = pixels[x,y]
            if r > 85 and g <= 40 and b <= 50:
                pixels[x,y] = (0,0,0) 
            elif r >= 200 and g >= 200 and b >= 200:
                pixels[x,y] = (255,255,255)
            else:
                pixels[x,y] = (255,0,0) 

def scaleDown(freq: float):
    div = 1e3
    while True:
        if len(str(int(freq/div))) < 4:
            break
        if str(freq/div).split('.')[1] != '0':
            break
        else:
            div *= 1e3
    return freq/div

# Listen to relative power around the centerFrequency
def listen(centerFrequency, byteCount=1024, sampleRate=1.2e6):
    from rtlsdr import RtlSdr
    sdr = RtlSdr()
    sdr.sample_rate = sampleRate
    sdr.center_freq = centerFrequency
    sdr.gain = 'auto'
    sample = sdr.read_bytes(byteCount*128)
    sdr.close()
    print(f'Sampled {byteCount} bytes')
    return sample

# Graph a power distribution sample into a line graph
def graph(sample, centerFrequency, title=None, xLabel=None, yLabel=None, sampleRate=1.2, size=(4.3,3.2), color='red', fileName='figure.png'):
    import matplotlib.pyplot as plt
    plt.figure(num=None, figsize=size) # screen is 3.33x2.5 inches, 400x300 pixels (4.3,3.2)
    plt.psd(x=sample, 
            NFFT=1024, 
            Fs=sampleRate, 
            Fc=scaleDown(centerFrequency), # only in FM rn
            color=color, 
            )
    if title != None:
        plt.title = title
    plt.xlabel(xLabel) 
    plt.ylabel(yLabel)
    plt.savefig(fileName, bbox_inches='tight') #, pad_inches=0)
    print(f'Generated figure {fileName} ({size[0]}x{size[1]} inches)')

# Display an image on the inky display
def display(imageFile='figure.png'):
    from PIL import Image
    img = Image.open(imageFile).convert('RGB')

    # color correct for the eink display
    colorCorrect(img)
    img = img.convert('P', palette=Image.ADAPTIVE)#, colors=3)
    print(f'Color-corrected {imageFile} for eink display')
 
    from inky.auto import auto
    display = auto()
    img = img.transpose(Image.FLIP_TOP_BOTTOM) #just because of how the screen sits on my desk
    img = img.transpose(Image.FLIP_LEFT_RIGHT)
    #img = img.resize(display.resolution)
    display.set_image(img)
    display.show()
    print(f'Displaying {imageFile}')