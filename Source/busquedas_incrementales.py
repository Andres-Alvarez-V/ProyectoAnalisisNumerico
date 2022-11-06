import numpy as np

# %Este programa encuentra un intervalo donde f(x) tiene cambio de signo
# %usando el método de búsquedas incrementales

# %Entradas: 
# %f, función continua
# %x0, punto inicial
# %h, paso
# %Nmax, número máximo de iteraciones

# %Salidas
# %a, extremo izquierdo del intervalo
# %b, extremo derecho del intervalo
# %iter, número de iteraciones

def funcion(x):
    #f=((x)**3)-(7.51*(x)**2)+(18.4239*(x))-14.8331
    f=(1/x)+(0.4)-(1.74*np.log(20*np.sqrt(x)))
#    f=90*(x+40)*(x+27)*(x+95)-50000000

    return f

def main():
    xi=float(input("Xi= "))
    deltax=float(input("Delta x= "))
    itemax=float(input("Itemax= "))
    fi=funcion(xi)
    xf=xi+deltax
    ff=funcion(xf)
    ite=0
    while(fi*ff>0 and itemax>ite):
        xi=xf
        fi=ff
        xf=xi+deltax
        ff=funcion(xf)
        ite+=1
    if fi*ff<0:
        print(f"Entre",xi,xf,"hay raiz")
    elif ff==0:
        print( xf,"raiz" )

    else:
        print( "No llegamos" )
if __name__=="__main__":
    main()
