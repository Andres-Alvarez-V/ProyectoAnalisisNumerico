# Método de Gauss-Seidel
# solución de sistemas de ecuaciones
# por métodos iterativos

# %Entradas: 
# %A, matrix invertible
# %b, vector constante
# %x0, aproximaci�n inicial 
# %tol, tolerancia
# %Nmax, n�mero m�ximo de iteraciones

# %Salidas
# %x, soluci�n
# %iter, n�mero de iteraciones
# %err, error


import numpy as np
def gauss_seidel(A,B,X0):
    tolera=int(input("Ingresar tolerancia: "))
    iteramax=int(input("Ingrese numero de iteraciones máxima "))
    # Gauss-Seidel
    tamano = np.shape(A)
    n = tamano[0]
    m = tamano[1]
    #  valores iniciales
    X = np.copy(X0)
    diferencia = np.ones(n, dtype=float)
    errado = 2*tolera

    itera = 0
    while not(errado<=tolera or itera>iteramax):
        print(f'iter : {itera}\n x: {X}\n lc : {diferencia}\n -----------------------------')
        # por fila
        for i in range(0,n,1):
            # por columna
            suma = 0 
            for j in range(0,m,1):
                # excepto diagonal de A
                if (i!=j): 
                    suma = suma-A[i,j]*X[j]
            nuevo = (B[i]+suma)/A[i,i]
            diferencia[i] = np.abs(nuevo-X[i])
            X[i] = nuevo
        errado = np.max(diferencia)
        itera = itera + 1

    # Respuesta X en columna
    X = np.transpose([X])

    # revisa si NO converge
    if (itera>iteramax):
        X=0
    # revisa respuesta
    verifica = np.dot(A,X)

    # SALIDA
    print('respuesta X: ')
    print(X)
    print('verificar A.X=B: ')
    print(verifica)
