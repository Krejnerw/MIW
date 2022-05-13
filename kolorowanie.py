# -*- coding: utf-8 -*-
"""
Created on Tue Mar 29 19:37:43 2022

@author: weron
"""

from math import sqrt
from random import choice

import numpy as np

data = []
with open("australian.dat", "r", encoding="utf-8") as f:
    for line in f:
        # print(line, end="")
        data.append(list(map(lambda x: float(x),line.split())))

def metryka2(vector1:list,vector2:list):
    v1 = np.array(vector1)
    v2 = np.array(vector2)
    a = v2-v1
    dot = np.dot(a,a)
    return sqrt(dot)


def check_covering(data, data2):
    covering = 0
    for i in range(len(data)):
        if data[i][-1] == data2[i][-1]:
            covering+=1
    return covering/len(data)*100
        
# covering = check_covering(data, data2)

# 2.
def segregate_data(data:[list])->dict:
    data_dict = {}
    for record in data:
        if record[-1] in data_dict:
            data_dict[record[-1]].append(record)
        else:
            data_dict[record[-1]] = [record]
    return data_dict

# 3.
def sumOfDistances(x, data):
    result = 0
    for record in data:
        result += metryka2(x, record)
    return result
    
def dictOfDistances(segregated_data:dict,data:[list])->dict:
    distances = {}
    for ind, record in enumerate(data):
        key = record[-1]
        if key not in distances:
            distances[key] = [(ind, sumOfDistances(record, segregated_data[key]))]
        else:
            distances[key].append((ind, sumOfDistances(record, segregated_data[key])))
    return distances

# data_dict = segregate_data(data)
# dist = dictOfDistances(data_dict, data)
        
# 4.
def mass_point(data):
    mass = {}
    for key in data.keys():
        for record in data[key]:
            if key not in mass:
                mass[key] = record
            else:
                if mass[key][1]>record[1]:
                    mass[key] = record
    return mass
            
# mass_points = mass_point(dist)

# 5.
def check_nearest_mass_point(data, mass_points):
    changes = 0
    for record in data:
        nearest = metryka2(record, data[list(mass_points.items())[0][1][0]])
        nearest_ind = list(mass_points.items())[0][1][0]
        for point in mass_points.items():
            ind = point[1][0]
            if metryka2(record, data[ind]) < nearest:
                nearest = metryka2(record, data[ind])
                nearest_ind = ind
        if data[nearest_ind][-1] != record[-1]:
            record[-1] = data[nearest_ind][-1]
            changes +=1
    return changes

# checked = check_nearest_mass_point(data, mass_points)
# 6. 
def koloruj(data2):
    while True:
        segregated = segregate_data(data2)
        distances = dictOfDistances(segregated, data2)
        mass_points = mass_point(distances)
        sumOfChanges = check_nearest_mass_point(data2, mass_points)
        if sumOfChanges == 0:
            break;

# 1. 
data2 = [x.copy() for x in data]

for record in data2:
    record[-1] = choice([0.,1.])
    
koloruj = koloruj(data2)
end_covering = check_covering(data, data2)
print(end_covering)

kl0=0
kl1=0
for i in data2:
    if i[-1] ==0:
        kl0+=1
    else:
        kl1+=1
print("0: ",kl0)
print("1: ",kl1)
                
    

