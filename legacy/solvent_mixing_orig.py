# Animation of solvent mixing

import numpy as np
import random as rd
from math import *
import matplotlib.pyplot as plt
from matplotlib import animation
import mixFuncs_orig as mix

fig = plt.figure(figsize=(8.0, 6.0))

lattice_x = 20
lattice_y = 10
idFinal = lattice_x * lattice_y

initConfig = mix.initConfig(lattice_x, lattice_y)
img = mix.drawPoints(lattice_x, lattice_y, idFinal, initConfig)
fig.savefig("./png/mixing0.png", dpi=300)

curConfig = initConfig

repNum = 10

stat = []

for i in range(repNum):
    probePoint = curConfig[45]
    stat.append(probePoint[1])
    newConfg = mix.exchangePairs(lattice_x, lattice_y, idFinal, curConfig)
    img = mix.drawPoints(lattice_x, lattice_y, idFinal, newConfg)
    fig.savefig("./png/mixing"+str(i+1)+".png", dpi=300)
    curConfig = newConfg

np.savetxt("./data/stat_list.txt", stat)

plt.show()
plt.close()