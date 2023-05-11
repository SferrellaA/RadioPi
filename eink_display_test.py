#!/usr/bin/python
from helpers import graphPSD, display
from numpy import random as np

freq = 0
sample = np.random(1024)

graphPSD(sample, freq)
display()
input("No title, x label, nor y label")

graphPSD(sample, freq, title="Title")
display()
input("Just the title")

graphPSD(sample, freq, xLabel="xlabel")
display()
input("Just the x label")

graphPSD(sample, freq, yLabel="ylabel")
display()
input("Just the y label")

graphPSD(sample, freq, title="Title", xLabel="xlabel")
display()
input("Title and x label")

graphPSD(sample, freq, title="Title", yLabel="ylabel")
display()
input("Title and y label")

graphPSD(sample, freq, title="Title", xLabel="xlabel", yLabel="ylabel")
display("Title, x label, and y label")