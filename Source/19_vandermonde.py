import numpy as np

X=[1,2,3,4]
Y=[0.2,2.6,8.6,20]

n=len(X)
A= np.zeros((n,n))

for i in range(n):
    for j in range(n):
        A[i,j]=X[i]**j

inversa=np.linalg.inv(A)

coef=[]
for i in range(n):
    contador=0
    for j in range(n):
        contador+=inversa[i,j]*Y[j]
    coef.append(contador)

frase="el polinomio que representa esta función es "
for i in range(len(coef)):
        if i==0:
            frase=frase+ str(coef[i])+"+"

        elif i==n-1:
            frase=frase+str(coef[i])+"x^"+str(i)
        else:
            frase=frase+str(coef[i])+"x^"+str(i)+"+"

print(frase)




