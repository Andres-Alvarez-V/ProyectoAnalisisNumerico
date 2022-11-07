
#partir el intervalo por la mitad y despues volver a hacer lo mismo
#y asi sucesivamente
import numpy as np



def biseccion(f):
    xi=float(input("Ingrese X izquierdo= "))
    xs=float(input("Ingrese X derecho= "))
    tol=float(input("Ingrese la Tolerancia= "))
    niter=float(input("Ingrese Numero de Iteraciones= "))
    fxi=f(xi)
    fxs=f(xs)
    if fxi==0:
        print(xi,"es raiz")
    elif fxs==0:
        print(xs,"es raiz")
    elif fxi*fxs<0:
        xm=(xi+xs)/2
        fxm=f(xm)
        cont=1
        error=tol+1
        #while fxi >0.0001 and fxm != 0 and cont<niter:
        while error>tol and fxm != 0 and cont<niter:
            if fxi*fxm<0:
                xs=xm
                fxs=fxm
                print("error",error)
                print("fxs = ",fxs,"----- Derecha")
                print("xs = ",xi)
                print("   ")

            else:
                xi=xm
                fxi=fxm
                print("error",error)
                print("fxi = ",fxm,"------- izquierda")
                print("xi = ",xi)
                print("   ")
            xaux=xm
            xm=(xi+xs)/2
            fxm=f(xm)
            error=abs(xm-xaux)
            cont+=1
        if fxm==0:
            print(xm ,"es raiz")
        elif error<tol:
            print(xm,"es una aproximacion con tolerancia =",tol)
        else:
            print("fracaso en ",niter,"iteraciones")
    else:
        print("El intervalo es inadecuado")


