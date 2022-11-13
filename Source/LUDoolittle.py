
import numpy as np
def doolittle(A,b):
    n = len(A)
    L = np.eye(n)
    U = np.eye(n)

    for i in range(n):
        for k in range(i, n):
            sum = 0;
            for j in range(i):
                sum += (L[i][j] * U[j][k]);
            U[i][k] = A[i][k] - sum;

        for k in range(i, n):
            sum = 0;
            for j in range(i):
                sum += (L[k][j] * U[j][i])
            L[k][i] = (A[k][i] - sum) /U[i][i]

    Z = np.linalg.solve(L, b)
    print(f'Z ->\n {Z}')
    x = np.linalg.solve(U, Z)

    print("Matrix L")
    print(L)
    print("Matrix U")
    print(U)
    print("Solution")
    print(x)
    print("Verify")
    print(np.dot(L,U))
