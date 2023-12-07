import numpy as np

def multiplicarMatriz(A, B):
    n = len(A)
    if n == 1:
        return A * B

    A_submatrizes = divide_matrix(A)
    B_submatrizes = divide_matrix(B)

    products = []
    for i in range(3):
        for j in range(3):
            products.append(multiplicarMatriz(A_submatrizes[i][j], B_submatrizes[i][j]))

    C = np.zeros((n, n))
    for i in range(3):
        for j in range(3):
            C[i * n // 3:(i + 1) * n // 3, j * n // 3:(j + 1) * n // 3] = products[i * 3 + j]

    return C

def divide_matrix(A):
    n = len(A)
    submatrizes = []
    for i in range(3):
        for j in range(3):
            submatrizes.append(A[i * n // 3:(i + 1) * n // 3, j * n // 3:(j + 1) * n // 3])
    return submatrizes


