# Entradas:
# A -> Matriz invertible
# b -> Vector de constntes

# Salidas:
# x -> Vector solución
# L, U -> Matrices de factorizacion
import numpy as np

# Ingreso
A = np.array([[36,3,-4,5],
              [5,-45,10,-2],
              [6,8,57,5],   
              [2,3,-8,-42]])

b = np.array([[-20],
              [69],
              [96],
              [-32]])

#Procedimiento
n = len(A)
L = np.eye(n)
U = np.eye(n)

for i in range(n):
    # Matriz L
    for k in range(i, n):
        # Producto Punto
        sum = 0;
        for j in range(i):
            sum += (L[k][j] * U[j][i])
        L[k][i] = A[k][i] - sum;

    # Matriz U
    for k in range(i, n):
        # Producto Punto
        sum = 0;
        for j in range(i):
            sum += (L[i][j] * U[j][k]);
        U[i][k] = (A[i][k] - sum) /L[i][i]

Z = np.linalg.solve(L, b)
x = np.linalg.solve(U, Z)

print("Matriz L")
print(L)
print("Matriz U")
print(U)
print("Solucion")
print(x)