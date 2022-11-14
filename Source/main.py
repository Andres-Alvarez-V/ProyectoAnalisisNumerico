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
    print(f"\nInsert the function \n")
    user_input = input("f(x) = ")
    user_input=user_input.replace("e","E")
    #print(re.sub("[1-9]+x","[1-9]*x", user_input))
    expr = sympify(user_input)
    f = lambdify(x, expr)
    return f
def ingresar_funcion2():
    x = var('x')  # the possible variable names must be known beforehand...
    print(f"\nInsert the function \n")
    user_input = input("g(x) = ")
    user_input=user_input.replace("e","E")
    #print(re.sub("[1-9]+x","[1-9]*x", user_input))
    expr = sympify(user_input)
    g = lambdify(x, expr)
    return g
def ingresar_derivada():
    x = var('x')  # the possible variable names must be known beforehand...
    print(f"\nInsert the derivative \n")
    user_input = input("f'(x) = ")
    user_input=user_input.replace("e","E")
    #print(re.sub("[1-9]+x","[1-9]*x", user_input))
    expr = sympify(user_input)
    f = lambdify(x, expr)
    return f

def ingresar_segunda_derivada():
    x = var('x')  # the possible variable names must be known beforehand...
    print(f"\nInsert the second derivative: \n")
    user_input = input("f''(x) = ")
    user_input=user_input.replace("e","E")
    #print(re.sub("[1-9]+x","[1-9]*x", user_input))
    expr = sympify(user_input)
    f = lambdify(x, expr)
    return f




def ingresar_matrizA():
    print(f"\nMatrix A")
    m = int(input(f"\nInsert the number of rows: "))
    n = int(input("Insert the number of colums: "))
    print(f"Insert by rows, writing the elements separated by spaces\n")
    A = []
    i=0
    while i<m:
        fila = list(map(float, input().split()))
        if len(fila)<m:
            print(f"\nIt must be real values, try again\n")
            i=0
            A=[]
        elif len(fila)>m:

            print(f"\nToo many values, try again\n")
            i=0
            A=[]
        else:
            A.append(fila)
            i+=1
    return np.array(A)


def ingresar_vectorb():
    print(f"\nVector b\n")
    n=int(input(f"Insert the vector dimension "))
    Flag=True
    while Flag:
        b = np.array(list(map(float,
                          input(f"\nInsert the vector b transposed: ").split())))
        if len(b)!=n:
            print("\nTry again\n")
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
    n=int(input(f"Insert the vector dimension"))
    Flag=True
    while Flag:
        b = np.array(list(map(float,
                          input(f"\nInsert the data of X ").split())))
        if len(b)!=n:
            print("\nTry again\n")
            b=[]
        else:
            return b


def ingresar_vectorY():
    print(f"\nVector Y\n")
    n=int(input(f"Insert the vector dimension "))
    Flag=True
    while Flag:
        b = np.array(list(map(float,
                          input(f"\nInsert the data of Y ").split())))
        if len(b)!=n:
            print("\nTry again\n")
            b=[]
        else:
            return b
def usuario():
    print(f"\nHello!, welcome to our program\n")
    table = [
    ["1.1 Crout","2.1 complete pivoting","3.1 Gauss-Seidel","4.1 Bisection","5.1 Vandermonde"],
    ["1.2 Doolittle","2.2 Gauss-Jordan simple ","3.2 Jacobi","4.2 False position"," "],
    ["1.3 Cholesky"," "," ","4.3 Fixed point"," "],
    ["1.4 Gauss-jordan elimination"," "," ","4.4 Newton"," "],
    ["1.5 Gauss-Jordan partial pivoting elimination " ," " ," " , "4.5 Secant", " "],
    [" "," "," ","4.6 Multiple roots"," "]
    ]
    print(tabulate(table, headers=["LU factorization","Direct methods", "Iterative methods", "Functions", "Interpolation"]))
    print(f"Insert the option of method you want \n \n")
    n=float(input(f"Option "))
    print("   ")
    return n

def elegir(n):
    if n == 1.1:
        print("Welcome to Crout")
        A=ingresar_matrizA()
        b=ingresar_vectorb()
        crout(A,b)
    elif n == 1.2:
        print("Welcome to Doolittle")
        A=ingresar_matrizA()
        b=ingresar_vectorb()
        doolittle(A,b)

    elif n == 1.3:
        print("Welcome to Cholesky")
        A=ingresar_matrizA()
        b=ingresar_vectorb()
        cholesky(A,b)

    elif n == 1.4 :
        print("Welcome to Gaussian fatorization")
        A=ingresar_matrizA()
        b=ingresar_vectorb()
        lusimpl(A,b)
    elif n==1.5:
        print("Welcome to partial Gaussian LU factorization")
        A=ingresar_matrizA()
        b=ingresar_vectorb()
        lupar(A,b)


    elif n == 2.1 :
        print("Welcome to partial pivoting")
        A=ingresar_matrizA()
        b=ingresar_vectorb()
        pivoteo_parcial(A,b)

    elif n ==2.2 :
        print("Welcome to simple Gaussian simplification")
        A=ingresar_matrizA()
        b=ingresar_vectorb()
        gaussiana_simple(A,b)

    elif n == 3.1:
        print("Welcome to Gauss-Seidel")
        A=ingresar_matrizA()
        b=ingresar_vectorb()
        gauss_seidel(A,b)
    elif n == 3.2:
        print("Welcome to Jacobi")
        A=ingresar_matrizA()
        b=ingresar_vectorb()
        Jacobi(A,b)
    elif n == 4.1 :
        print(f"Welcome to bisection")
        f=ingresar_funcion()
        biseccion(f)
    elif n == 4.2:
        print("Welcome to false position")
        f=ingresar_funcion()
        reglafalsa(f)
    elif n == 4.3:
        print("Welcome to fixed point")
        f=ingresar_funcion2()
        puntofijo(f)
    elif n == 4.4 :
        print("Welcome to newton")
        f=ingresar_funcion()
        g=ingresar_funcion2()
        newton(f,g)
    elif n == 4.5:
        print("Welcome to secant")
        f=ingresar_funcion()
        secante(f)
    elif n == 4.6:
        print("Welcome to multiple roots")
        f=ingresar_funcion()
        df=ingresar_derivada()
        d2f=ingresar_segunda_derivada()
        raices_multiples(f,df,d2f)
    elif n==5.1:
        print("Welcome to Vandermonde")
        X=ingresar_vectorX()
        Y=ingresar_vectorY()
        vandermonde(X,Y)
    else:
        print("Invalid option, try again")
        n=usuario()
        elegir(n)


def main():
    n=usuario()
    elegir(n)
if __name__ == "__main__":
    main()
