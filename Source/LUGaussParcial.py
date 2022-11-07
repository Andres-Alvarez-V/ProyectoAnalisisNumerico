import numpy as np
from sustregr import sustregr
from sustprgr import sustprgr

def lupar(A, vb):
    n = A.shape[0]
    L = np.eye(n)
    U = np.zeros((n,n))
    P = np.eye(n)
    M = A.astype(float)
    for i in range(n-1):
        print(M)
        [a,b] = np.where(np.abs(M)==np.max(np.abs(M[i:,i:n])))
        print(a)
        print(b)
        print(np.abs(M))
        print(np.abs(M)==np.max(np.abs(M[i:,i:n])))
        print(np.max(np.abs(M[i:,i:n])))
        print(".................................")
        if a[0] != i:
            M[[i,a[0]],:]=M[[a[0],i],:]
            P[[i,a[0]],:]=P[[a[0],i],:]
            if i > 0:
                L[[i,a[0]],0:i]=L[[a[0],i],0:i]
        for j in range(i+1,n):
            if M[j,i] != 0:
                L[j,i]=M[j,i]/M[i,i]
                M[j,i:n]=M[j,i:n]-(M[j,i]/M[i,i])*M[i,i:n]
        U[i,i:n]=M[i,i:n];
        U[i+1,i+1:n]=M[i+1,i+1:n]

    U[n-1,n-1]=M[n-1,n-1]

    L = np.insert(L, L.shape[0],np.matmul(P,vb),axis=1).astype(float)
    z = sustprgr(L)
    U = np.insert(U, U.shape[0],z,axis=1).astype(float)
    x = sustregr(U)
    return x

