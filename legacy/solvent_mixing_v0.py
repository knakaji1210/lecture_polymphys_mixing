# 

import numpy as np
import random as rd
from math import *
import matplotlib.pyplot as plt
from matplotlib import animation
import mixFuncs as mix

fig = plt.figure()

ax = fig.add_subplot(111,title='', xlabel='X', ylabel='Y',
                      xlim=[-10, 10], ylim=[-5, 5])

ax.set_xticks(np.linspace(-10, 10, 21))
ax.set_xticklabels([])

ax.set_yticks(np.linspace(-5, 5, 11))
ax.set_yticklabels([])

plt.grid(b=True, which='major', color='#999999', linestyle='-')

# initial configuration

numBlue = 0
numRed = 0
idNum = 1
idFinal = 200
particles_list = []
imgs = []

for i in range(10):
    for j in range(10):
        x = i-9.5
        y = j-4.5
        coordinate = [x, y]
        idParticle = [idNum, 0, coordinate]
        idNum+=1
        numBlue+=1
        particles_list.append(idParticle)

for i in range(10):
    for j in range(10):
        x = i+0.5
        y = j-4.5
        coordinate = [x, y]
        idParticle = [idNum, 1, coordinate]
        idNum+=1
        numRed+=1
        particles_list.append(idParticle)

mix.drawPoints(idFinal, particles_list, ax)
#imgs.append(img)
fig.savefig("./png/img0.png", dpi=300)

M = 10

for m in range(M):
    mix.exchange(particles_list)
    mix.drawPoints(idFinal, particles_list, ax)
    filetext = 'img'+str(m)
    fig.savefig("./png/"+filetext+".png", dpi=300)
    #imgs.append(img)

#img = mix.drawPoints(idFinal, particles_list, ax)
#imgs.append(img)
#fig.savefig("./png/update.png", dpi=300)

#print(len(imgs))

#ani = animation.ArtistAnimation(fig, imgs, interval=10)
#ani.save('./gif/mixing.gif', writer = 'pillow', fps = 30)

plt.show()