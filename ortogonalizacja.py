# -*- coding: utf-8 -*-
"""
Created on Tue Apr 26 17:26:28 2022

@author: weron
"""
from math import sqrt

import numpy as np


def policz_dl_vectora(vector_u):
    """Oblicza dlugosc vektora"""
    suma = sum([pow(u,2) for u in vector_u])
    return sqrt(suma)
    
def policz_e(vector_u):
    """Oblicza wartosc wektora u przy dlugosci 1"""
    dl = policz_dl_vectora(vector_u)
    return vector_u/dl

def projekcja_vektora(vector_v, vector_u):
    """Oblicza projekcje konkretnych vektorow"""
    nominator = np.dot(vector_v,vector_u)
    denominator = np.dot(vector_u,vector_u)        
    return nominator/denominator * vector_u

def projekcje_u_dla_v(vector_v, lista_u):
    """Oblicza wektor u dla wektora v i wczesniejszych u"""
    suma_projekcji = vector_v.copy()
    for vector_u in lista_u:
        suma_projekcji -= projekcja_vektora(vector_v, vector_u) 
    return suma_projekcji

def macierz_Q(macierz):
    """Zwraca macierz Q - kwadratowa macierz ortogonalna"""
    lista_u = [macierz.T[0]]
    q = [policz_e(lista_u[0])]
    for vector_v in macierz.T[1:]:
        u = projekcje_u_dla_v(vector_v, lista_u)
        q.append(policz_e(u))
        lista_u.append(u)
    return np.array(q).T 
    # return np.around(np.array(q).T,6)   
    
def macierz_R(macierz):
    """zwraca macierz R - gorna macierz trojkatna - qTa"""
    q = macierz_Q(macierz)
    return np.dot(q.T,macierz)
    # return np.around(np.dot(q.T,macierz),5)

def macierz_A_z_QR(macierz_q, macierz_r):
    """zwraca macierz pierwotna - dr jakodekompozycja macierzy"""
    return np.dot(macierz_q,macierz_r)
    # return np.around(np.dot(macierz_q,macierz_r),5)

def is_matrix_upper_triangular(matrix):
    for ind, vector in enumerate(matrix):
        if sum(vector[:ind]) != 0:
            print("suma z ind ", ind," :",sum(vector[:ind]))
            print(vector)
            return False
    return True

macierz_a = [[2., 1., 3.],[1., 6., 7.],[3., 7., 9.]]
macierz_d = [[0., 1., 2.],[1., 0., 7.],[9., 7., 9.]]
macierz_b = [[2., 1., 3.],[0., 6., 7.],[0., 0., 9.]]
x = [[2.,1.],[1.,0.],[0.,1.]]

macierz_c = np.array(x)

macierz_q = macierz_Q(macierz_c.copy())
macierz_r = macierz_R(macierz_c.copy())

macierz_qr = macierz_A_z_QR(macierz_q.copy(), macierz_r.copy())

print("macierz A: ",macierz_c, sep="\n")
print("macierz Q: ",macierz_q, sep="\n")
print("macierz R: ",macierz_r, sep="\n")
print("macierz QR = A: ",np.around(macierz_qr,1), sep="\n")
