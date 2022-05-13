# -*- coding: utf-8 -*-
"""
Created on Mon Apr  4 18:00:17 2022

@author: weron
"""
import numpy as np


def read_points(file_name="points.txt", mode="r"):
    x = []
    y = []
    with open(file_name, mode, encoding="utf-8") as f:
        for line in f:
            a = line[1:-2]
            b = list(map(lambda i: float(i),a.split(",")))
            y.append([b[1]])
            x.append([1,b[0]])
    return x,y

def transpose(matrix):
    result = []
    columns_count = len(matrix[0])
    for i in range(columns_count):
            result.append([])
            
    for i in matrix:
        for j in range(len(i)):
            result[j].append(i[j])
            
    return result

def rotation_matrix(matrix):
    det = matrix[0][0]*matrix[1][1]-matrix[0][1]*matrix[1][0]
    xD = np.array([[1,1],[1,1]]) 

    for i in range(0,2):
        for j in range(0,2):
            xD[i][j] = pow(-1,i+j+2)*matrix[1-i][1-j]

    xTx1 = transpose(xD)/det
    return xTx1
    
def linear_regression(vector_x, vector_y):
    # x*b = y ==> x/x*b = 1/x*y dzielenie lewostr
    # b = (xTx)^(-1)xTy
    x = np.array(vector_x)
    y = np.array(vector_y)

    xTx = np.dot(transpose(x), x)
    rotate_xTx = rotation_matrix(xTx)           
    
    xTy = np.dot(transpose(x),y)
    return rotate_xTx.dot(xTy)
    
# wynik [2/7 i 5/14] = [0,2857142857142857, 0,3571428571428571]
# dla [(2,1),(5,2),(7,3)(8,3)]

x,y = read_points()
lin_regres = linear_regression(x, y)

print(lin_regres)
