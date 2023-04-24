# Functions necessary to calculate solvent mixing

import numpy as np
import random as rd
from math import *
import matplotlib.pyplot as plt

def initialConfig(lattice_x, lattice_y):

# function for initial configuration

    num_blue = 0
    num_red = 0
    point_id = 0
    initConfig = []
    point_status = [0,1]

    for i in range(int(lattice_x / 2)):
        for j in range(int(lattice_y)):
            x = i - (lattice_x / 2 - 0.5)
            y = j - (lattice_y / 2 - 0.5)
            point_coordinate = [x, y]
            point_attribute = [point_id, point_status[0], point_coordinate]
            point_id+=1
            num_blue+=1
            initConfig.append(point_attribute)

    for i in range(int(lattice_x / 2)):
        for j in range(int(lattice_y)):
            x = i + 0.5
            y = j - (lattice_y / 2 - 0.5)
            point_coordinate = [x, y]
            point_attribute = [point_id, point_status[1], point_coordinate]
            point_id+=1
            num_blue+=1
            initConfig.append(point_attribute)
    return initConfig


def exchangePairs(lattice_x, lattice_y, end_point_id, currentConfig):

    direction_list = ['n', 's', 'e', 'w']

    for i in range(end_point_id):
        point1_attribute = currentConfig[i]
        point1_id = point1_attribute[0]
        point_exchange = rd.choice(direction_list)
        if point_exchange == 'n':
            if point1_id % lattice_y == lattice_y - 1:
                pass
            else:
                point2_attribute = currentConfig[i+1]
                point1_status = point1_attribute[1]
                point2_status = point2_attribute[1]
                point1_attribute[1] = point2_status
                point2_attribute[1] = point1_status
        if point_exchange == 's':
            if point1_id % lattice_y == 0:
                pass
            else:
                point2_attribute = currentConfig[i-1]
                point1_status = point1_attribute[1]
                point2_status = point2_attribute[1]
                point1_attribute[1] = point2_status
                point2_attribute[1] = point1_status
        if point_exchange == 'e':
            if  (lattice_x - 1)*lattice_y - 1 < point1_id:
                pass
            else:
                point2_attribute = currentConfig[i + lattice_y]
                point1_status = point1_attribute[1]
                point2_status = point2_attribute[1]
                point1_attribute[1] = point2_status
                point2_attribute[1] = point1_status
        if point_exchange == 'w':
            if point1_id <= lattice_y:
                pass
            else:
                point2_attribute = currentConfig[i - lattice_y]
                point1_status = point1_attribute[1]
                point2_status = point2_attribute[1]
                point1_attribute[1] = point2_status
                point2_attribute[1] = point1_status
    return currentConfig


def drawPoints(end_point_id, currentConfig):

    x_blue_list = []
    y_blue_list = []
    x_red_list = []
    y_red_list = []
    imgs = []

    for i in range(end_point_id):
        point_attribute = currentConfig[i]
        if point_attribute[1] == 0:
            point_coordinate = point_attribute[2]
            x = point_coordinate[0]
            y = point_coordinate[1]
            x_blue_list.append(x) 
            y_blue_list.append(y)
        if point_attribute[1] == 1:
            point_coordinate = point_attribute[2]
            x = point_coordinate[0]
            y = point_coordinate[1]
            x_red_list.append(x) 
            y_red_list.append(y)
    img_blue = plt.plot(x_blue_list, y_blue_list, linestyle = "", marker=".", color="blue")
    img_red = plt.plot(x_red_list, y_red_list, linestyle = "", marker=".", color="red")
    img = img_blue + img_red
    imgs.append(img)
    return imgs


def drawStepEvolutionFunc(maxPoints, x_orig_list, y_orig_list):

    x_list = []
    y_list = []

    for i in range(maxPoints):
        x_list.append(x_orig_list[:i+1])
        y_list.append(y_orig_list[:i+1])

    return x_list, y_list