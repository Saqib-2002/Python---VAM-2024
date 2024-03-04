# How to work on live data set and display in graph?
import matplotlib.pyplot as mp
import random as rn
from matplotlib.animation import FuncAnimation
from itertools import count

x = []
y = []
repeatCount = count()
def liveDataSet(i):
    x.append(next(repeatCount))
    y.append(rn.randint(0, 20))
    mp.cla
    mp.plot(x, y)
    mp.show()
myPlotFunc = FuncAnimation(mp.gcf(), liveDataSet, interval = 100)
mp.show()