import numpy as np
def newton(f,g):
    x0=float(input("Ingrese x inicial "))
    tol=float(input("Ingrese la tolerancia "))
    niter=int(input("Ingrese el número máximo de iteraciones "))
    fx=f(x0)
    dfx=g(x0)
    cont=0
    error=tol+1
    while error >tol and fx!= 0 and dfx!=0 and cont<niter:
        x1=x0-(fx/dfx)
        fx=f(x1)
        # print(abs(fx))
        dfx=g(x1)
        error=abs(x1-x0)
        x0=x1
        cont+=1
        # print(x0)
    if fx==0:
        print(x0," es raiz ")
    elif error<tol:
        (x1, " es una aproximacion a una iraz con una tolerancia de: ",tol)
    elif dfx==0:
        print(x1," es una posible raiz multiple ")
    else:
        print("fracaso en", niter,"iteraciones")

def main():
    x0=float(input("X0 "))
    tol=float(input("Tol "))
    nmax=int(input("niter "))
    newton(x0,tol,nmax)

if __name__ == '__main__':
    main()
