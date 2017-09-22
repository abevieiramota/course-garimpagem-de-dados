import numpy as np
from lsh_compose import compose
from matplotlib import pyplot as plt
from ipywidgets import *

fig = plt.figure(figsize=(10, 6))
ax = fig.add_subplot(1, 1, 1)

ax.plot([0, 10], [0, 0])
l1, = ax.plot([0, 2.5], [.1, .1])
ax.plot([0, 0], [0, .1])
ax.plot([5, 5], [0, .1])
ax.plot([10, 10], [0, .1])

@interact(ini=(0, 5, .1))
def plot_line_buckets(ini = 0):
    
    l1.set_xdata((ini, ini + 2.5))
    fig.canvas.draw()

fig.show()