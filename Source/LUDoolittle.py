# Entradas:
# A -> Matriz invertible
# b -> Vector de constntes

# Salidas:
# x -> Vector solución
# L, U -> Matrices de factorizacion
import numpy as np
def doolittle(A,b):
    n = len(A)
    L = np.eye(n)
    U = np.eye(n)

    for i in range(n):
        # Matriz U
        for k in range(i, n):
            # Producto Punto
            sum = 0;
            for j in range(i):
                sum += (L[i][j] * U[j][k]);
            U[i][k] = A[i][k] - sum;

        # Matriz L
        for k in range(i, n):
            # Producto Punto
            sum = 0;
            for j in range(i):
                sum += (L[k][j] * U[j][i])
            L[k][i] = (A[k][i] - sum) /U[i][i]

    Z = np.linalg.solve(L, b)
    print(f'Z ->\n {Z}')
    x = np.linalg.solve(U, Z)

    print("Matriz L")
    print(L)
    print("Matriz U")
    print(U)
    print("Solucion")
    print(x)
    print("Verifica")
    print(np.dot(L,U))
