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


def busquedas(f):
    xi=float(input("Ingrese x inicial= "))
    deltax=float(input("Ingrese delta x= "))
    itemax=float(input("Ingrese N iteraciones máximas= "))
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
