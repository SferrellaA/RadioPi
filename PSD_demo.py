#!/usr/bin/python
from sys import argv
from helpers import frequency, listen, graphPSD, display

# Select the frequency
f = "433.3mhz"
if len(argv) > 1:
    f = argv[1]
freq = frequency(f)
print(f"Listening on {f}")

# The demo
sample = listen(freq, 5)
graphPSD(sample, freq, title=f"{f} Capture")
display()
