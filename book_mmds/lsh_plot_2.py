import numpy as np
from lsh_compose import compose
from matplotlib import pyplot as plt
from ipywidgets import *

ini_p1 = .2
ini_p2 = .7

x = np.linspace(0, 1, 100)
_, f = compose('')

fig = plt.figure(figsize=(10, 6))
ax = fig.add_subplot(1, 1, 1)
linef, = ax.plot(x, f(x))
linep1, = ax.plot((ini_p1, ini_p1), (0, 1))
linep2, = ax.plot((ini_p2, ini_p2), (0, 1))

ax.set_ylabel("Probabilidade final")
ax.set_xlabel("Probabilidade inicial")

@interact(a = (1, 20), o = (1, 20), p1 = (0., 1., .01), p2 = (0., 1., .01))
def update(a = 1, o = 1, p1 = ini_p1, p2 = ini_p2):
    try:
        nfuns, f = compose('a{0}o{1}'.format(a, o))
        linef.set_ydata(f(x))
        linep1.set_xdata([p1])
        linep2.set_xdata([p2])
        fig.canvas.draw()
        ax.set_title('funções necessárias = {}\np1, p2 = ({}, {})\nfp1, fp2 = ({:.2f}, {:.2f})'.format(nfuns,
                                                                           p1, p2,
                                                                           f(p1), f(p2)))
    except:
        None
        
fig.show()