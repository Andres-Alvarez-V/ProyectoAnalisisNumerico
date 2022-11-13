from biseccion import biseccion #necesita funcion
from busquedas_incrementales import busquedas #necesita funcion
from LUCholesky import cholesky
from LuCrout import crout
from LUDoolittle import doolittle
from LUGaussParcial import lupar
from LuGaussSimpl import lusimpl #necesita A y b  
from metodo_raices_multiples import raices_multiples #funcion,derivada,segunda
from MetodoGaussianaPivoteParcial import pivoteo_parcial
from MetodoGaussianaSimple import gaussiana_simple
from MetodoGaussSeidel import gauss_seidel
from MetodoJacobi import Jacobi
from newton import newton
from puntofijo import puntofijo
from reglafalsa import reglafalsa
from secante import secante
from Vandermonde import vandermonde
import numpy as np
from sympy import var
from sympy import sympify
from sympy.utilities.lambdify import lambdify
import re
from tabulate import tabulate

def ingresar_funcion():
    x = var('x')  # the possible variable names must be known beforehand...
    print(f"\nIngrese la función \n")
    user_input = input("f(x) = ")
    user_input=user_input.replace("e","E")
    #print(re.sub("[1-9]+x","[1-9]*x", user_input))
    expr = sympify(user_input)
    f = lambdify(x, expr)
    return f
def ingresar_funcion2():
    x = var('x')  # the possible variable names must be known beforehand...
    print(f"\nIngrese la función \n")
    user_input = input("g(x) = ")
    user_input=user_input.replace("e","E")
    #print(re.sub("[1-9]+x","[1-9]*x", user_input))
    expr = sympify(user_input)
    g = lambdify(x, expr)
    return g
def ingresar_derivada():
    x = var('x')  # the possible variable names must be known beforehand...
    print(f"\nIngrese la derivada \n")
    user_input = input("f'(x) = ")
    user_input=user_input.replace("e","E")
    #print(re.sub("[1-9]+x","[1-9]*x", user_input))
    expr = sympify(user_input)
    f = lambdify(x, expr)
    return f

def ingresar_segunda_derivada():
    x = var('x')  # the possible variable names must be known beforehand...
    print(f"\nIngrese la segunda derivada: \n")
    user_input = input("f''(x) = ")
    user_input=user_input.replace("e","E")
    #print(re.sub("[1-9]+x","[1-9]*x", user_input))
    expr = sympify(user_input)
    f = lambdify(x, expr)
    return f




def ingresar_matrizA():
    print(f"\nMatriz A")
    m = int(input(f"\nEntre el numero de filas: "))
    n = int(input("Entre el numero de columnas: "))
    print(f"Ingrese por filas, escribiendo los elementos separados por espacio\n")
    A = []
    i=0
    while i<m:
        fila = list(map(float, input().split()))
        if len(fila)<m:
            print(f"\nDeben ser valores reales, reintente\n")
            i=0
            A=[]
        elif len(fila)>m:

            print(f"\nDemasiados valores, reintente\n")
            i=0
            A=[]
        else:
            A.append(fila)
            i+=1
    return np.array(A)


def ingresar_vectorb():
    print(f"\nVector b\n")
    n=int(input(f"Ingrese la dimension del vector "))
    Flag=True
    while Flag:
        b = np.array(list(map(float,
                          input(f"\nIngrese el vector b tranpuesto: ").split())))
        if len(b)!=n:
            print("\nReitente\n")
            b=[]
        else:
            m=b.shape[0]
            b=b.reshape((m,1))
            print("    ")
            print(b)
            print("    ")
            return b

def ingresar_vectorX():
    print(f"\nVector X\n")
    n=int(input(f"Ingrese la dimension del vector "))
    Flag=True
    while Flag:
        b = np.array(list(map(float,
                          input(f"\nIngrese los datos de X: ").split())))
        if len(b)!=n:
            print("\nReitente\n")
            b=[]
        else:
            return b


def ingresar_vectorY():
    print(f"\nVector Y\n")
    n=int(input(f"Ingrese la dimension del vector "))
    Flag=True
    while Flag:
        b = np.array(list(map(float,
                          input(f"\nIngrese los datos de Y ").split())))
        if len(b)!=n:
            print("\nReitente\n")
            b=[]
        else:
            return b
def usuario():
    print(f"\nHola!, bienvenido a nuestro programa\n")
    table = [
    ["1.1 Crout","2.1 Pivoteo total","3.1 Gauss-Seidel","4.1 Biseccion","5.1 Vandermonde"],
    ["1.2 Doolittle","2.2 Gauss simple ","3.2 Jacobi","4.2 Regla falsa"," "],
    ["1.3 Cholesky"," "," ","4.3 Punto fijo"," "],
    ["1.4 Gauss simple"," "," ","4.4 Newton"," "],
    ["1.5 Gauss parcial " ," " ," " , "4.5 Secante", " "],
    [" "," "," ","4.6 Raices múltiples"," "]
    ]
    print(tabulate(table, headers=["Factorizacion LU","Metodos directos", "Metodos iterativos", "Funciones", "Interpolacion"]))
    print(f"Ingrese la opcion del método que desee \n \n")
    n=float(input(f"Opcion "))
    print("   ")
    return n

def elegir(n):
    if n == 1.1:
        print("Bienvenido a Crout")
        A=ingresar_matrizA()
        b=ingresar_vectorb()
        crout(A,b)
    elif n == 1.2:
        print("Bienvenido a Doolittle")
        A=ingresar_matrizA()
        b=ingresar_vectorb()
        doolittle(A,b)

    elif n == 1.3:
        print("Bienvenido a Cholesky")
        A=ingresar_matrizA()
        b=ingresar_vectorb()
        cholesky(A,b)

    elif n == 1.4 :
        print("Bienvenido a factorizacion gaussiana")
        A=ingresar_matrizA()
        b=ingresar_vectorb()
        lusimpl(A,b)
    elif n==1.5:
        print("Bienvenido a factorizacion LU gaussiana parcial")
        A=ingresar_matrizA()
        b=ingresar_vectorb()
        lupar(A,b)


    elif n == 2.1 :
        print("Bienvenido a Pivoteo parcial")
        A=ingresar_matrizA()
        b=ingresar_vectorb()
        pivoteo_parcial(A,b)

    elif n ==2.2 :
        print("Bienvenido a simplificacion gaussiana simple")
        A=ingresar_matrizA()
        b=ingresar_vectorb()
        gaussiana_simple(A,b)

    elif n == 3.1:
        print("Bienvenido a Gauss-Seidel")
        A=ingresar_matrizA()
        b=ingresar_vectorb()
        gauss_seidel(A,b)
    elif n == 3.2:
        print("Bienvenido a Jacobi")
        A=ingresar_matrizA()
        b=ingresar_vectorb()
        Jacobi(A,b)
    elif n == 4.1 :
        print(f"Bienvenido a biseccion")
        f=ingresar_funcion()
        biseccion(f)
    elif n == 4.2:
        print("Bienvenido a regla falsa")
        f=ingresar_funcion()
        reglafalsa(f)
    elif n == 4.3:
        print("Bienvenido a punto fijo")
        f=ingresar_funcion2()
        puntofijo(f)
    elif n == 4.4 :
        print("Bienvenido a newton")
        f=ingresar_funcion()
        g=ingresar_funcion2()
        newton(f,g)
    elif n == 4.5:
        print("Bienvenido a secante")
        f=ingresar_funcion()
        secante(f)
    elif n == 4.6:
        print("Bienvenido a raíces múltiples")
        f=ingresar_funcion()
        df=ingresar_derivada()
        d2f=ingresar_segunda_derivada()
        raices_multiples(f,df,d2f)
    elif n==5.1:
        print("Bienvenido a Vandermonde")
        X=ingresar_vectorX()
        Y=ingresar_vectorY()
        vandermonde(X,Y)
    else:
        print("Opcion invalida, intente de nuevo")
        n=usuario()
        elegir(n)


def main():
    n=usuario()
    elegir(n)
if __name__ == "__main__":
    main()
