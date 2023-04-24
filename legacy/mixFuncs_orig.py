# 

import numpy as np
import random as rd
from math import *
import matplotlib.pyplot as plt

def initConfig(lattice_x, lattice_y):
    numBlue = 0
    numRed = 0
    idNum = 0
    initConfig = []

    for i in range(int(lattice_x / 2)):
        for j in range(int(lattice_y)):
            x = i - (lattice_x / 2 - 0.5)
            y = j - (lattice_y / 2 - 0.5)
            coordinate = [x, y]
            idParticle = [idNum, 0, coordinate]
            idNum+=1
            numBlue+=1
            initConfig.append(idParticle)

    for i in range(int(lattice_x / 2)):
        for j in range(int(lattice_y)):
            x = i + 0.5
            y = j - (lattice_y / 2 - 0.5)
            coordinate = [x, y]
            idParticle = [idNum, 1, coordinate]
            idNum+=1
            numRed+=1
            initConfig.append(idParticle)
    return initConfig


def drawPoints(lattice_x, lattice_y, idFinal, configList):

    xRange = lattice_x/2
    yRange = lattice_y/2

    plt.title('Solvent Mixing')
    plt.xlabel('X')
    plt.ylabel('Y')
#    plt.xticks(np.linspace(-xRange, xRange, lattice_x + 1))
#    plt.yticks(np.linspace(-yRange, yRange, lattice_y + 1))
    plt.xticks(np.linspace(-xRange, xRange, 5))
    plt.yticks(np.linspace(-yRange, yRange, 5))
    plt.xlim(-xRange, xRange)
    plt.ylim(-yRange, yRange)
    #plt.grid(b=True, which='major', color='#999999', linestyle='-')

    for n in range(idFinal):
        idParticle_temp = configList[n]
        if idParticle_temp[1] == 0:
            coordinate = idParticle_temp[2]
            x = coordinate[0]
            y = coordinate[1]
            img = plt.plot(x, y, marker=".", color="blue")
        if idParticle_temp[1] == 1:
            coordinate = idParticle_temp[2]
            x = coordinate[0]
            y = coordinate[1]
            img = plt.plot(x, y, marker=".", color="red")
    return img

def exchangePairs(lattice_x, lattice_y, idFinal, configList):

    direction_list = ['n', 's', 'e', 'w']

    for i in range(idFinal):
        idParticle1 = configList[i]
        id = idParticle1[0]
        exchange = rd.choice(direction_list)
        if exchange == 'n':
            if id % lattice_y == lattice_y - 1:
                pass
            else:
                idParticle2 = configList[i+1]
                stat1 = idParticle1[1]
                stat2 = idParticle2[1]
                idParticle1[1] = stat2
                idParticle2[1] = stat1
        if exchange == 's':
            if id % lattice_y == 0:
                pass
            else:
                idParticle2 = configList[i-1]
                stat1 = idParticle1[1]
                stat2 = idParticle2[1]
                idParticle1[1] = stat2
                idParticle2[1] = stat1
        if exchange == 'e':
            if  (lattice_x - 1)*lattice_y - 1 < id:
                pass
            else:
                idParticle2 = configList[i + lattice_y]
                stat1 = idParticle1[1]
                stat2 = idParticle2[1]
                idParticle1[1] = stat2
                idParticle2[1] = stat1
        if exchange == 'w':
            if id <= lattice_y:
                pass
            else:
                idParticle2 = configList[i - lattice_y]
                stat1 = idParticle1[1]
                stat2 = idParticle2[1]
                idParticle1[1] = stat2
                idParticle2[1] = stat1
    return configList