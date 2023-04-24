# Animation of solvent mixing

import numpy as np
import random as rd
from math import *
import matplotlib.pyplot as plt
from matplotlib import animation
import mixFuncs as mix

fig = plt.figure(figsize=(8.0, 6.0))

lattice_x = 40
lattice_y = 20
idFinal = lattice_x * lattice_y

xRange = lattice_x/2
yRange = lattice_y/2

ax1 = fig.add_subplot(111, title='Solvent Mixing', xlabel='X', ylabel='Y',
        xlim=[-xRange, xRange], ylim=[-yRange , yRange])
#ax1.set_xticks(np.linspace(-xRange, xRange, lattice_x + 1))
#x1.set_yticks(np.linspace(-yRange, yRange, lattice_y + 1))
ax1.set_xticks(np.linspace(-xRange, xRange, 5))
ax1.set_yticks(np.linspace(-yRange, yRange, 5))
#ax1.grid(b=True, which='major', color='#999999', linestyle='-')

imgs_rep = []

initConfig = mix.initConfig(lattice_x, lattice_y)
imgs = mix.drawPoints(idFinal, initConfig)
imgs_rep = imgs_rep + imgs
#fig.savefig("./png/mixing0.png", dpi=300)

curConfig = initConfig

repNum = 10

#stat = []

for i in range(repNum):
    #probePoint = curConfig[45]
    #stat.append(probePoint[1])
    newConfg = mix.exchangePairs(lattice_x, lattice_y, idFinal, curConfig)
    imgs = mix.drawPoints(idFinal, newConfg)
    imgs_rep = imgs_rep + imgs
    fig.savefig("./png/mixing_test"+str(i+1)+".png", dpi=300)
    curConfig = newConfg


ani = animation.ArtistAnimation(fig, imgs_rep, interval=500)
ani.save('./gif/solvent_mixing.gif', writer = 'pillow', fps = 30)

plt.show()
plt.close()