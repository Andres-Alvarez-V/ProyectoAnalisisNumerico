import numpy as np

def f(x):
    f=np.exp(3*x-12)+x*np.cos(3*x)-x**2+4
    return f

x0 = float(input("X1= "))
x1 = float(input("X0= "))
tol = float(input("Tol= "))
Nmax = float(input("N Max= "))
fx0 = f(x0)
fx1 = f(x1)
if fx0 == 0:
    print(x0,"es raiz")
elif fx1 == 0:
    print(x1,"es raiz")
else:
    cont = 1
    error = tol + 1
    #while fx0 >0.0001 and fxm != 0 and cont<Nmax:
    while error>tol and cont<Nmax:
        xaux = x1 - (fx1*(x1 - x0)/(fx1 - fx0))
        faux = f(xaux)
        error=abs(xaux - x1)
        cont += 1
        x0 = x1
        fx0 = fx1
        x1 = xaux
        fx1 = faux

    if faux == 0:
        print(xaux ,"es raiz")
    elif error < tol:
        print(xaux,"es una aprox0macion con tolerancia =",tol)
    else:
        print("fracaso en ",Nmax,"iteraciones")