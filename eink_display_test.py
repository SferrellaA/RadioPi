#!/usr/bin/python
'''
matplotlib graphics are precision-pixel, so 
resizing them to fit a screen makes it not look right. 
Rendering a graph at the correct size is best.

matplotlib only considers the visualization part of a
graph towards the generated image's size hoewver. So 
the title and axis labels can cause the graph to be
incorrectly sized.

Generating graphs of different sizes helps ensure 
they fit an inky what correctly.
'''

# Imports
from helpers import graphPSD, display
from numpy import random as np
from random import random

# Generate random data for a figure
freq = random()
sample = np.random(1024)

'''
The inky what takes a few seconds to display, so 
descriptions of each rendering are put in input()
calls so the user can continue after they've seen 
the screen rander
'''
print("For each rendering, press enter to continue")

# The graphPSD and display functions don't *need* filenames...
print("Graphing no title, x label, nor y label")
graphPSD(sample, freq)
display()
input("\npress [enter] to continue")

# ... but both will accept a specific file to display
print("Graphing just the title")
figure = "figure.png"
graphPSD(sample, freq, title="Title", fileName=figure)
display(figure)
input("\npress [enter] to continue")

# graphPSD will return the file it saved to if you want
print("Graphing just the x label")
figure = graphPSD(sample, freq, xLabel="xlabel")
display(figure)
input("\npress [enter] to continue")

# It's default filename is "figure.png" 
print("Graphing just the y label")
graphPSD(sample, freq, yLabel="ylabel")
display("figure.png")
input("\npress [enter] to continue")

# Python lets you nest one function's output as another's input
print("Graphing title and x label")
display(graphPSD(sample, freq, title="Title", xLabel="xlabel"))
input("\npress [enter] to continue")

# There's many you can make your code run
print("Graphing title and y label")
figure = "figure.png"
figure = graphPSD(sample, freq, title="Title", yLabel="ylabel", fileName="figure.png")
display("figure.png")
input("\npress [enter] to continue")

# But simple is also nice
print("Graphing title, x label, and y label")
graphPSD(sample, freq, title="Title", xLabel="xlabel", yLabel="ylabel")
display()
input("\npress [enter] to continue")
