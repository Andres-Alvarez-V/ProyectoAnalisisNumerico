


import numpy as np
def gauss_seidel(A,B,X0):
    tolera=int(input("Tolerance: "))
    iteramax=int(input("Max iterations "))
    # Gauss-Seidel
    tamano = np.shape(A)
    n = tamano[0]
    m = tamano[1]
    X = np.copy(X0)
    diferencia = np.ones(n, dtype=float)
    errado = 2*tolera

    itera = 0
    while not(errado<=tolera or itera>iteramax):
        print(f'iter : {itera}\n x: {X}\n lc : {diferencia}\n -----------------------------')
        for i in range(0,n,1):
            suma = 0 
            for j in range(0,m,1):
                if (i!=j): 
                    suma = suma-A[i,j]*X[j]
            nuevo = (B[i]+suma)/A[i,i]
            diferencia[i] = np.abs(nuevo-X[i])
            X[i] = nuevo
        errado = np.max(diferencia)
        itera = itera + 1

    X = np.transpose([X])

    if (itera>iteramax):
        X=0
    verifica = np.dot(A,X)

    print('X: ')
    print(X)
    print('verify A.X=B: ')
    print(verifica)
