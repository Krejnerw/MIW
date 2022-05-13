# -*- coding: utf-8 -*-
"""
Created on Tue Apr 26 13:16:33 2022

@author: weron
"""

import numpy as np

from ortogonalizacja import macierz_A_z_QR, macierz_Q, macierz_R


def is_matrix_upper_triangular(matrix):
    for ind, vector in enumerate(matrix):
        if sum(vector[:ind]) > 0.000001:
            print("suma z ind ", ind," :",sum(vector[:ind]))
            print(vector)
            return False
    return True

def ak_next(ak):
    q = macierz_Q(ak)
    r = macierz_R(ak)
    ak = macierz_A_z_QR(r, q)
    return ak

def find_matrix_eigenvalues(matrix):
    ak = matrix
    is_upper_triangular = is_matrix_upper_triangular(ak)

    while(not is_upper_triangular):
        ak = ak_next(ak)
        is_upper_triangular = is_matrix_upper_triangular(ak)
    return np.diag(ak)


macierz_a = [[2., 1., 3.],[1., 6., 7.],[3., 7., 9.]]
macierz_d = [[0., 1., 2.],[1., 0., 7.],[9., 7., 9.]]
macierz_b = [[2., 1., 3.],[0., 6., 7.],[0., 0., 9.]]

macierz_c = np.array(macierz_b)

macierz_q = macierz_Q(macierz_c.copy())
macierz_r = macierz_R(macierz_c.copy())

macierz_qr = macierz_A_z_QR(macierz_q.copy(), macierz_r.copy())

print("macierz A: ",macierz_c, sep="\n")
print("macierz Q: ",macierz_q, sep="\n")
print("macierz R: ",macierz_r, sep="\n")
print("macierz QR = A: ",np.around(macierz_qr,1), sep="\n")
# -----------------------------------------------------------------
wlasne = find_matrix_eigenvalues(macierz_c.copy())
print("--------------------------------------------",wlasne,sep="\n")
print(np.linalg.eigvals(macierz_c.copy()))
