# -*- coding: utf-8 -*-
"""
Created on Mon Apr  4 18:00:17 2022

@author: weron
"""
from math import sqrt

import numpy as np


def read_data_from_file(file_name="australian.dat", mode="r"):
    data = []
    with open(file_name, mode, encoding="utf-8") as f:
        for line in f:
            # print(line, end="")
            data.append(list(map(lambda x: float(x),)))
    return data

def arithmetic_mean_of_vector(vector:list)->float:
    n = len(vector)
    ones = np.ones(n)
    return np.dot(vector,ones)/n

def variance_of_vector(vector:list)->float:
    """count vector variance for population"""
    n = len(vector)
    mean = arithmetic_mean_of_vector(vector)*np.ones(n)
    a = vector-mean
    variance = np.dot(a, a)/len(vector)
    return variance

def standard_deviation_of_vector(vector:list)->float:
    """count standard deviation for population"""
    return sqrt(variance_of_vector(vector))

vector = [10,12,9,1,3,4.5,9.2]
print("mean: ", arithmetic_mean_of_vector(vector))
print("variance: ", variance_of_vector(vector))
print("deviation: ",standard_deviation_of_vector(vector))
