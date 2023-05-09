from helpers import graph, display
from numpy import random as np

freq = 0
sample = np.random(1024)

graph(sample, freq)
display()
input("No title, x label, nor y label")

graph(sample, freq, title="Title")
display()
input("Just the title")

graph(sample, freq, xLabel="xlabel")
display()
input("Just the x label")

graph(sample, freq, yLabel="ylabel")
display()
input("Just the y label")

graph(sample, freq, title="Title", xLabel="xlabel")
display()
input("Title and x label")

graph(sample, freq, title="Title", yLabel="ylabel")
display()
input("Title and y label")

graph(sample, freq, title="Title", xLabel="xlabel", yLabel="ylabel")
display("Title, x label, and y label")