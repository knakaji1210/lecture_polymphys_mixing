# Functions necessary to calculate solvent mixing

import numpy as np
import random as rd
from math import *
import matplotlib.pyplot as plt

def initialConfig(lattice_x, lattice_y):

# function for initial configuration

#   num_blue = 0            # 青い粒子の数、使われていないのでコメントアウトする
#   num_red = 0             # 赤い粒子の数、使われていないのでコメントアウトする
    point_id = 0            # 各格子点のID
    initConfig = []         # 初期配列の格納庫
    point_status = [0,1]    # 粒子の状態　青：0、赤：1

# 格子点の左半分に青い粒子を敷き詰める
    for i in range(int(lattice_x / 2)):     # 左下から右上に向かって行く
        for j in range(int(lattice_y)):
            x = i - (lattice_x / 2 - 0.5)
            y = j - (lattice_y / 2 - 0.5)
            point_coordinate = [x, y]
            point_attribute = [point_id, point_status[0], point_coordinate] # 各格子点の属性（ID、粒子の状態、xy座標）を格納
#           print(point_attribute)
            point_id+=1
#           num_blue+=1
            initConfig.append(point_attribute)

# 格子点の右半分に赤い粒子を敷き詰める
    for i in range(int(lattice_x / 2)):
        for j in range(int(lattice_y)):
            x = i + 0.5
            y = j - (lattice_y / 2 - 0.5)
            point_coordinate = [x, y]
            point_attribute = [point_id, point_status[1], point_coordinate] # ID、粒子の状態、xy座標を格納
#           print(point_attribute)
            point_id+=1     # IDはリセットされず、さらに追加されていく
#           num_red+=1
            initConfig.append(point_attribute)
    return initConfig


def exchangePairs(lattice_x, lattice_y, end_point_id, currentConfig):

    direction_list = ['n', 's', 'e', 'w']               # 東西南北へ移動する可能性

    for i in range(end_point_id):
        point1_attribute = currentConfig[i]             # i番目の格子点の属性を抽出
        point1_id = point1_attribute[0]                 # i番目の格子点のID
        point_exchange = rd.choice(direction_list)      # 移動する方向をランダムに決定
        if point_exchange == 'n':                       # 移動する方向が「北」のとき
            if point1_id % lattice_y == lattice_y - 1:  # 一番上の格子点を除外
                pass
            else:
                point2_attribute = currentConfig[i+1]   # (i+1)番目の格子点（北にある）の属性を抽出
                point1_status = point1_attribute[1]     # i番目の格子点の粒子の状態を抽出
                point2_status = point2_attribute[1]     # (i+1)番目の格子点の粒子の状態を抽出
                point1_attribute[1] = point2_status     # 状態を交換
                point2_attribute[1] = point1_status
        if point_exchange == 's':                       # 移動する方向が「南」のとき
            if point1_id % lattice_y == 0:              # 一番下の格子点を除外
                pass
            else:
                point2_attribute = currentConfig[i-1]   # (i-1)番目の格子点（南にある）の属性を抽出
                point1_status = point1_attribute[1]
                point2_status = point2_attribute[1]
                point1_attribute[1] = point2_status
                point2_attribute[1] = point1_status
        if point_exchange == 'e':                       # 移動する方向が「東」のとき
            if  (lattice_x - 1)*lattice_y - 1 < point1_id:  # 一番右の格子点を除外
                pass
            else:
                point2_attribute = currentConfig[i + lattice_y] # (i+lattice_y)番目の格子点（東にある）の属性を抽出
                point1_status = point1_attribute[1]
                point2_status = point2_attribute[1]
                point1_attribute[1] = point2_status
                point2_attribute[1] = point1_status
        if point_exchange == 'w':                       # 移動する方向が「西」のとき
            if point1_id <= lattice_y:                  # 一番左の格子点を除外
                pass
            else:
                point2_attribute = currentConfig[i - lattice_y] # (i-lattice_y)番目の格子点（西にある）の属性を抽出
                point1_status = point1_attribute[1]
                point2_status = point2_attribute[1]
                point1_attribute[1] = point2_status
                point2_attribute[1] = point1_status
    return currentConfig


def pointsCoordinates(end_point_id, currentConfig):

    x_blue = []                                     # 青い粒子群のx座標を格納
    y_blue = []                                     # 青い粒子群のy座標を格納
    x_red = []                                      # 赤い粒子群のx座標を格納
    y_red = []                                      # 赤い粒子群のy座標を格納
    imgs = []

    for i in range(end_point_id):
        point_attribute = currentConfig[i]          # 全ての格子点について各格子点の属性を抽出
        if point_attribute[1] == 0:                 # その格子点の属性のうち、粒子の状態が青なら
            point_coordinate = point_attribute[2]   # その格子点のxy座標を抽出
            x = point_coordinate[0]
            y = point_coordinate[1]
            x_blue.append(x)
            y_blue.append(y)
        if point_attribute[1] == 1:                 # その格子点の属性のうち、粒子の状態が赤なら
            point_coordinate = point_attribute[2]
            x = point_coordinate[0]
            y = point_coordinate[1]
            x_red.append(x) 
            y_red.append(y)

    pointsCoordinates = [x_blue, y_blue, x_red, y_red]

    return pointsCoordinates

def probePointMean(probe_point_id, lattice_y, currentConfig):
    probe_point_status = []
    id = probe_point_id
    ly = lattice_y
    probe_point_ids = [id-2*ly-2, id-2*ly-1, id-2*ly, id-2*ly+1, id-2*ly+2, 
                       id-ly-2, id-ly-1, id-ly, id-ly+1, id-ly+2, 
                       id-2, id-1, id, id+1, id+2, 
                       id+ly-2, id+ly-1, id+ly, id+ly+1, id+ly+2, 
                       id+2*ly-2, id+2*ly-1, id+2*ly, id+2*ly+1, id+2*ly+2]    # プローブ点を中心にした25点のID
    for i in probe_point_ids:
        probe_point = currentConfig[i]
        probe_point_status.append(probe_point[1])
    probe_point_status_mean = np.mean(probe_point_status)                                   # プローブ点を中心にした9点の状態の平均
    return probe_point_status_mean

def drawStepEvolutionFunc(maxPoints, x_orig_list, y_orig_list):     # アニメーション用のリストのリストを作る

    x_list = []
    y_list = []

    for i in range(maxPoints+1):
        x_list.append(x_orig_list[:i+1])
        y_list.append(y_orig_list[:i+1])

    return x_list, y_list