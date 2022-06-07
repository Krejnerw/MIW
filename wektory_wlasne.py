import numpy as np

from wartosci_wlasne import find_matrix_eigenvalues


def gauss(matrix):
    size = len(matrix[0])
    for i in range(size - 1):
        divider = matrix[i][i]

        for j in range(i, size):
            if divider == 0:
                raise ZeroDivisionError()

            matrix[i][j] = matrix[i][j] / divider
            # matrix[i][j] = np.round(matrix[i][j]/divider, 4)

        for y in range(i + 1, size):
            first = matrix[y][i]

            for x in range(i, size):
                matrix[y][x] = matrix[y][x] - first * matrix[i][x]
                # matrix[y][x] = np.round(matrix[y][x] - first * matrix[i][x],3)
    for y in range(size - 2, 0, -1):
        for i in range(y - 1, -1, -1):
            multi = matrix[i][y]
            row = matrix[y] * multi
            matrix[i] -= row

    return [np.round(matrix[y][size - 1], 3) for y in range(size - 1)]


def eigenvectors(matrix):
    u = []
    size = len(matrix[0])
    matrix_eigenvalues = find_matrix_eigenvalues(matrix)
    for eigenvalue in sorted(matrix_eigenvalues, reverse=True):
        # print("=== ", eigenvalue, " ================")

        temp_matrix = matrix.copy()
        for i in range(size):
            temp_matrix[i][i] = np.round(temp_matrix[i][i] - eigenvalue, 3)

        gauss1 = gauss(temp_matrix)

        wek_wlasn = [round(y * -1, 4) for y in gauss1] + [1]
        u.append(wek_wlasn)
        # print("***wektor wlasny: ***")
        # print(
        #     wek_wlasn,
        #     "\n",
        # )
    u = np.array(u)
    return u


# a = [
#     [1.0, 2.0, 3.0, 4.0, 5.0],
#     [2.0, 2.0, 3.0, 4.0, 5.0],
#     [3.0, 3.0, 3.0, 4.0, 5.0],
#     [4.0, 4.0, 4.0, 4.0, 5.0],
#     [5.0, 5.0, 5.0, 5.0, 5.0],
# ]
# b = [[-26.0, -33.0, -25.0], [31.0, 42.0, 23.0], [-11.0, -15.0, -4.0]]
# matrix = np.array(b)

# c = [[1.,2.,0.],[2.,0.,2.]]
# c = np.array(c)
# matrix = np.dot(c,c.T)

# print(eigenvectors(matrix))

# ===  19.598  ================
# ***wektor wlasny: ***
# [0.645, 0.678, 0.745, 0.851, 1]
#    +      +       +      +

# ===  -3.185  ================
# ***wektor wlasny: ***
# [-1.152, -0.79, -0.181, 0.486, 1]
#      +      +       +     +

# ===  -0.75  ================
# ***wektor wlasny: ***
# [1.109, -0.37, -1.355, -0.534, 1]
#    +      +    -1.356     +

# ===  -0.385  ================ > -0.386
# ***wektor wlasny: ***
# [-1.098, 1.755, 0.05, -1.785, 1]
#  -1.102  1.756  0.062 -1.793

# ===  -0.277  ================
# ***wektor wlasny: ***
# [1.106, -2.887, 3.542, -2.816, 1]
#  1.100  -2.873  3.528  -2.811
