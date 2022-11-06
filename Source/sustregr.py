import numpy as np

def sustregr(M):
    n = M.shape[0]
    x = np.zeros((n,1))
    for i in range(n-1,-1,-1):
        temp = 0
        for j in range(0,n):
            temp += M[i,j] * x[j,0]
        x[i,0] = (M[i,n] - temp) / M[i,i]
    return x.flatten()