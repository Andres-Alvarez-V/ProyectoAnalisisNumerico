

import numpy as np
def pivoteo_parcial(A,B):
    casicero = 1e-15 # Considerar como 0

    # Evitar truncamiento en operaciones
    A = np.array(A,dtype=float)

    # Matriz aumentada
    AB  = np.concatenate((A,B),axis=1)
    AB0 = np.copy(AB)

    # Pivoteo parcial por filas
    tamano = np.shape(AB)
    n = tamano[0]
    m = tamano[1]

    # Para cada fila en AB
    for i in range(0,n-1,1):
        # columna desde diagonal i en adelante
        columna  = abs(AB[i:,i])
        print(AB)
        print(columna)
        dondemax = np.argmax(columna)
        print(dondemax)
        print("-----------------------------")
        # dondemax no está en diagonal
        if (dondemax !=0):
            # intercambia filas
            temporal = np.copy(AB[i,:])
            AB[i,:] = AB[dondemax+i,:]
            AB[dondemax+i,:] = temporal
    AB1 = np.copy(AB)

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


    # SALIDA
    print('Expanded matrix:')
    print(AB0)
    print('For rows')
    print(AB1)
    print('Forward elimination')
    print(AB)
    print('Solution: ')
    print(X)
