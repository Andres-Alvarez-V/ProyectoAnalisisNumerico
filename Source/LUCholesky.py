# inputs:
# A -> Invertible Matrix 
# b -> resources vector

# Salidas:
# x -> solution
# L, U -> decomposition 

from math import sqrt
import numpy as np

def cholesky(A,b):
    n = len(A)
    L = np.eye(n)
    U = np.eye(n)

    for i in range(n):
        sum = 0
        for j in range(i):
            sum += (L[i][j] * U[j][i])
        L[i][i] = sqrt(abs(A[i][i] - sum))
        U[i][i] = L[i][i]
        # Matrix U
        for k in range(i, n):
            # dot product
            sum = 0;
            for j in range(i):
                sum += (L[k][j] * U[j][i])
            L[k][i] = (A[k][i] - sum)/U[i][i];

        # Matrix L
        for k in range(i, n):
            # dot product
            sum = 0;
            for j in range(i):
                sum += (L[i][j] * U[j][k]);
            U[i][k] = (A[i][k] - sum) /L[i][i]

    Z = np.linalg.solve(L, b)
    x = np.linalg.solve(U, Z)

    print("Matrix L")
    print(L)
    print("Matrix U")
    print(U)
    print("Solution")
    print(x)
    return L,U,x
