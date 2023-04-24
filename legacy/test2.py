# Animation of solvent mixing

import numpy as np
import random as rd
from math import *
import matplotlib.pyplot as plt
from matplotlib import animation
import testFuncs2 as test

maxPoints = 100
numExt = 20

imgs_rep = []

fig = plt.figure(figsize=(8.0, 6.0))
ax = fig.add_subplot(111, title='test', xlabel='x', ylabel='y')

choice_list = [0, 1]

status = []

for i in range(maxPoints):
    statusPoint = rd.choice(choice_list)
    status.append(statusPoint)

t_list = []
stat_mean = []

for i in range(maxPoints):
    status_ext = []
    if i > maxPoints - numExt:
        pass
    else:
        for j in range(numExt):
            status_ext.append(status[i+j])
    t_list.append(i)
    stat_mean.append(np.mean(status_ext))

print(len(t_list))
print(len(stat_mean))

imgs = test.drawFunc(maxPoints, t_list, stat_mean)
imgs_rep = imgs_rep + imgs

ani = animation.ArtistAnimation(fig, imgs_rep, interval=200)
ani.save('./gif/test.gif', writer = 'pillow', fps = 10)

plt.show()
plt.close()