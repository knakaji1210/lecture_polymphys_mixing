# Animation of solvent mixing

import numpy as np
import random as rd
from math import *
import matplotlib.pyplot as plt
from matplotlib import animation
import testFuncs as test

maxPoints = 100

imgs_rep = []

fig = plt.figure(figsize=(8.0, 6.0))
ax = fig.add_subplot(111, title='test', xlabel='x', ylabel='y')

imgs = test.drawPoints(maxPoints)
imgs_rep = imgs_rep + imgs

ani = animation.ArtistAnimation(fig, imgs_rep, interval=500)
ani.save('./gif/test.gif', writer = 'pillow', fps = 10)

plt.show()
plt.close()