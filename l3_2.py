# -*- coding: utf-8 -*-
"""
Created on Wed Mar  9 11:42:44 2022

@author: weron
"""
import random
from math import sqrt

import numpy as np

# mapowanie 
tab = ["oln","wawa","gdansk","pozn","sosnowiec"]
# uzywajac map oraz lambda uzyskaj liste z 1. literami
first_letters = map(lambda x: x[:3], tab)
# print(list(first_letters))

# wczytanie danych z pliku i konvert na float
data = []
with open("australian.dat", "r", encoding="utf-8") as f:
    for line in f:
        # print(line, end="")
        data.append(list(map(lambda x: float(x),line.split())))

for i in data:
    i[-1] = random.randrange(0.0, 2.0, 1.0)

def metryka_euklidesowa(a:list, b:list):
    c = 0
    tmp = 0
    for i in range(max(len(b),len(a))-1):
        tmp = pow(a[i]-b[i],2)
        c += tmp
    return round(sqrt(c),3)


#  dom - funkcja, która policzy odleglosc zb = data ob= wiersz
# policz odlg dla kazdego elem tego zbioru 
# y = zb[0]
# policz odlg dl(x,y) gdzie x nalezy do zb/{zb[0]} tzn. dla kazdego elem oprocz 0
# pogrupowac wzgl klasy decyzyjnej tzn if x = 0 to odlg trafi do slownika {0:[lista odlg],1:[lista odlg], itd...}
def zbior_odleglosci_decyzji(record:list, data:[list]):
    zbior = {}
    for i in data:
        decyzja = int(i[-1])
        if decyzja not in zbior:
            zbior[decyzja] = [metryka_euklidesowa(record, i)]
        else:
            zbior[decyzja].append(metryka_euklidesowa(record, i))
    return zbior
# test metryki i slownika
# print("metryka:",metryka_euklidesowa(data[0], data[5]),sep="\n")
# print(metryka_euklidesowa(data[0], data[10]))
# print(metryka_euklidesowa(data[0], data[20]))

# print("zbiór:",zbior_odleglosci_decyzji(data[0],data[1:6]),sep="\n")
# print(zbior_odleglosci_decyzji(data[0],data[1:11]))
# print(zbior_odleglosci_decyzji(data[0],data[1:21]))

# test dla rekordu własnego
record = [1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0]  
slownik_dlugosci = zbior_odleglosci_decyzji(record, data)

# print(slownik_dlugosci[0][:5])
# print(slownik_dlugosci[1][:5])


# def find_decision(record:list,data:[list]):
#     zbior_odleglosci = zbior_odleglosci_decyzji(record, data)
#     key = list(zbior_odleglosci.keys())[0]
#     value = zbior_odleglosci[key][0]
    
#     for i in list(zbior_odleglosci.keys()):
#         for j in zbior_odleglosci[i]:
#             if j<value:
#                 value = j
#                 key = i
#     return value, key

# value, key = find_decision(record, data)
# print(value,key)

def metryka(x:list, data:[list]):
    zbior = []
    for j in data:
        c = 0
        for i in range(max(len(x),len(j))-1):
            c += pow(x[i]-j[i],2)
        zbior.append((j[-1],round(sqrt(c),4)))
    return zbior

def metryka2(vector1:list,vector2:list):
    v1 = np.array(vector1)
    v2 = np.array(vector2)
    a = v2-v1
    dot = np.dot(a,a)
    return sqrt(dot)

# print(metryka_euklidesowa([1,1], [2,3]))
# print(metryka2([1,1], [2,3]))

zbior_tupli = metryka(record,data)

def grupujemy(zbior_tupli:[tuple]):
    zbior = {}
    for i in zbior_tupli:
        decyzja = int(i[0])
        if decyzja not in zbior:
            zbior[decyzja] = [i[1]]
        else:
            zbior[decyzja].append(i[1])
    return zbior

def nn_do_klas(zbior_odleglosci:dict, k:int):
    zbior = {}
    for key in zbior_odleglosci.keys():
        zbior[key] = sum(sorted(zbior_odleglosci[key])[:k])
        # zbior[key] = round(zbior[key])/len(zbior[key]),4)
    return zbior

def zdefiniuj_klase(zbior:dict):
    sorted_zbior = sorted(zbior.items(),key=lambda x: x[1])
    if len(sorted_zbior)==1 or sorted_zbior[0][1] != sorted_zbior[1][1]:
        return sorted_zbior[0][0]
    else:
        return None

pogrupowane = grupujemy(zbior_tupli)
# print("pogrupowane: ",pogrupowane,sep="\n")
nn_odleglosci = nn_do_klas(pogrupowane,5)
# print(nn_odleglosci)
klasa = zdefiniuj_klase(nn_odleglosci)
print(klasa)
