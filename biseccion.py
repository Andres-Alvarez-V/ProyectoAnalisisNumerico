
#partir el intervalo por la mitad y despues volver a hacer lo mismo
#y asi sucesivamente
import numpy as np
def f(x):
#    f=((x)**3)-(7.51*(x)**2)+(18.4239*(x))-14.8331
#    f=90*(x+40)*(x+27)*(x+95)-50000000
    #f=(1/x)+(0.4)-(1.74*np.log(20*np.sqrt(x)))
    f=np.exp(3*x-12)+x*np.cos(3*x)-x**2+4
    return f


def main():
    xi=float(input("Xi= "))
    xs=float(input("Xs= "))
    tol=float(input("Tol= "))
    niter=float(input("N Iter= "))
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


if __name__=="__main__":
    main()
    
