from math import sqrt

import numpy as np

a = [
    [1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0],
    [1.0, 1.0, 1.0, 1.0, -1.0, -1.0, -1.0, -1.0],
    [1.0, 1.0, -1.0, -1.0, 0.0, 0.0, 0.0, 0.0],
    [0.0, 0.0, 0.0, 0.0, 1.0, 1.0, -1.0, -1.0],
    [1.0, -1.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0],
    [0.0, 0.0, 1.0, -1.0, 0.0, 0.0, 0.0, 0.0],
    [0.0, 0.0, 0.0, 0.0, 1.0, -1.0, 0.0, 0.0],
    [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 1.0, -1.0],
]
matrix = np.array(a)

diagonalna = matrix.dot(matrix.T)

print("--------diagonalna-----------", diagonalna, sep="\n")

ortonormalna = matrix.copy()
for i, v in enumerate(ortonormalna):
    w = sqrt(np.dot(v.T, v))
    ortonormalna[i] = ortonormalna[i] / w

print("--------ortonormalna-----------", np.round(ortonormalna, 3), sep="\n")


jednostkowa_diag = np.dot(ortonormalna.copy(), ortonormalna.copy().T)
print("--------jednost diag-----------", np.round(jednostkowa_diag, 0), sep="\n")

# a*x = 1
# x = a^(-1)

# xb = BTxa
b = [8, 6, 2, 3, 4, 6, 6, 5]

x = np.round(np.dot(ortonormalna, b), 3)
y = np.round(np.dot(x.T, x), 3)
print("--------x-----------", x, sep="\n")
print("--------y-----------", y, sep="\n")
