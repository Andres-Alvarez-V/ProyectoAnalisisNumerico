# %Entradas: 
# %A, matrix invertible
# %b, vector constante

# %Salidas
# %x, soluci�n

# Método de Gauss
# Solución a Sistemas de Ecuaciones
# de la forma A.X=B

import numpy as np
def gaussiana_simple(A,B):
    casicero = 1e-15 # Considerar como 0

    # Evitar truncamiento en operaciones
    A = np.array(A,dtype=float) 

    # Matriz aumentada
    AB  = np.concatenate((A,B),axis=1)

    tamano = np.shape(AB)
    n = tamano[0]
    m = tamano[1]


    # eliminación hacia adelante
    for i in range(0,n-1,1):
        pivote   = AB[i,i]
        adelante = i + 1
        for k in range(adelante,n,1):
            factor  = AB[k,i]/pivote
            AB[k,:] = AB[k,:] - AB[i,:]*factor
            

    # sustitución hacia atrás
    ultfila = n-1
    ultcolumna = m-1
    X = np.zeros(n,dtype=float)

    for i in range(ultfila,0-1,-1):
        suma = 0
        for j in range(i+1,ultcolumna,1):
            suma = suma + AB[i,j]*X[j]
        b = AB[i,ultcolumna]
        X[i] = (b-suma)/AB[i,i]

    X = np.transpose([X])


    print("Matriz resultante AB: ")
    print(AB)
    print("SOlucion:")
    print(X)
