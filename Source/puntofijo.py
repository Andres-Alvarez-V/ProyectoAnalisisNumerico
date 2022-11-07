import numpy as np



def puntofijo(g):
    x0=float(input("Ingrese x inicial "))
    tol=float(input("Ingrese la tolerancia "))
    nmax=int(input("Ingrese el número máximo de iteraciones "))
    xant=x0
    e=tol+1
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
