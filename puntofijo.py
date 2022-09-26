import numpy as np


def g(x):
    f=np.log((x**2)-(2*x)+2)
    #f=np.exp(-x)
    return f

def puntofijo(x0,tol,nmax):
    xant=x0
    e=1000
    contador=0

    while (tol<e and contador<=nmax):
        xact=g(xant)
        e=np.abs(xant-xact)
        contador+=1
        xant=xact

    if e>tol:
        print("no pudimos llegar a esa tolerancia con ",contador,"iteraciones")
    else:
        print("hubo ",contador," iteraciones y la raiz se encuentra en ",xant," con un error de ", e)


def main():
    tol=float(input("¿qué tolerancia necesitas? "))
    x0=float(input("¿en qué valor deseas iniciar? "))
    nmax=int(input("¿cuál es el número máximo de iteraciones permitidas? "))
    puntofijo(x0,tol,nmax)

if __name__ == '__main__':
    main()
