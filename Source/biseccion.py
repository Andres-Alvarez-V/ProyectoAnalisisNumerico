
#partir el intervalo por la mitad y despues volver a hacer lo mismo
#y asi sucesivamente
import numpy as np



def biseccion(f):
    xi=float(input("Left x= "))
    xs=float(input("Right x= "))
    tol=float(input("Tolerance= "))
    niter=float(input("Max iterations= "))
    fxi=f(xi)
    fxs=f(xs)
    if fxi==0:
        print(xi,"is root")
    elif fxs==0:
        print(xs,"is root")
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
                print("fxs = ",fxs,"----- Right")
                print("xs = ",xi)
                print("   ")

            else:
                xi=xm
                fxi=fxm
                print("error",error)
                print("fxi = ",fxm,"------- Left")
                print("xi = ",xi)
                print("   ")
            xaux=xm
            xm=(xi+xs)/2
            fxm=f(xm)
            error=abs(xm-xaux)
            cont+=1
        if fxm==0:
            print(xm ,"is root")
        elif error<tol:
            print(xm,"eits an approximation with tolerance =",tol)
        else:
            print("Fail in ",niter,"iterations")
    else:
        print("The interval is not right")


