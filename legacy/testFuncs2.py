# 

import numpy as np
import random as rd
from math import *
import matplotlib.pyplot as plt


def drawFunc(repNum, xorig_list, yorig_list):

    x_list = []
    y_list = []
    imgs = []

    for n in range(repNum):
        x = xorig_list[n]
        y = yorig_list[n]
        x_list.append(x) 
        y_list.append(y)
        img = plt.plot(x_list, y_list, color="cyan")
        imgs.append(img)
    return imgs

