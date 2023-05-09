from sys import argv
from helpers import *

# Select the frequency
f = "433.3mhz"
if len(argv) > 1:
    f = argv[1]
freq = frequency(f)
print(f"Listenign on {f}")

# The demo
sample = listen(freq)
graph(sample, freq, title=f"{f} Capture")
display()
