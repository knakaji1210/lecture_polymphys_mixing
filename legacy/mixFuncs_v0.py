# 

import numpy as np
import random as rd
from math import *
import matplotlib.pyplot as plt

def initConfig():
    numBlue = 0
    numRed = 0
    idNum = 1
    initConfig = []

    for i in range(10):
        for j in range(10):
            x = i-9.5
            y = j-4.5
            coordinate = [x, y]
            idParticle = [idNum, 0, coordinate]
            idNum+=1
            numBlue+=1
            initConfig.append(idParticle)

    for i in range(10):
        for j in range(10):
            x = i+0.5
            y = j-4.5
            coordinate = [x, y]
            idParticle = [idNum, 1, coordinate]
            idNum+=1
            numRed+=1
            initConfig.append(idParticle)
    return initConfig


def drawPoints(idFinal, configList):

    plt.title('')
    plt.xlabel('X')
    plt.ylabel('Y')
    plt.xticks(np.linspace(-10, 10, 21))
    plt.yticks(np.linspace(-5, 5, 11))
    plt.xlim(-10, 10)
    plt.ylim(-5, 5)

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

def exchangePairs(configList):

    direction_list = ['n', 's', 'e', 'w']

#    id = rd.randrange(1, 190, 1)
    for id in range(190):
        exchange = rd.choice(direction_list)
        if exchange == 'n':
            if id % 10 == 0:
                pass
            else:
                idParticle1 = configList[id]
                idParticle2 = configList[id+1]
#                print(idParticle1)
#                print(idParticle2)
                stat1 = idParticle1[1]
                stat2 = idParticle2[1]
                idParticle1[1] = stat2
                idParticle2[1] = stat1
#                print(idParticle1)
#                print(idParticle2)
        if exchange == 's':
            if id % 10 == 1:
                pass
            else:
                idParticle1 = configList[id]
                idParticle2 = configList[id-1]
                stat1 = idParticle1[1]
                stat2 = idParticle2[1]
                idParticle1[1] = stat2
                idParticle2[1] = stat1
        if exchange == 'e':
            if 191 <= id <= 200:
                pass
            else:
                idParticle1 = configList[id]
                idParticle2 = configList[id+10]
                stat1 = idParticle1[1]
                stat2 = idParticle2[1]
                idParticle1[1] = stat2
                idParticle2[1] = stat1
        if exchange == 'w':
            if 1 <= id <= 10:
                pass
            else:
                idParticle1 = configList[id]
                idParticle2 = configList[id-10]
                stat1 = idParticle1[1]
                stat2 = idParticle2[1]
                idParticle1[1] = stat2
                idParticle2[1] = stat1
    return configList