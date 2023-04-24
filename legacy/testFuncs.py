# 

import numpy as np
import random as rd
from math import *
import matplotlib.pyplot as plt


def drawPoints(maxPoints):

    x_list = []
    y_list = []
    imgs = []

    for n in range(maxPoints):
        x = n
        y = np.sqrt(n)
        x_list.append(x) 
        y_list.append(y)
        print(x_list)
        img = plt.plot(x_list, y_list, linestyle = "", marker=".", color="blue")
        imgs.append(img)
    return imgs

