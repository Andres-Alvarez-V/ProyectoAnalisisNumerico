# https://programmerclick.com/article/1094577006/

# %A, matrix invertible
# %b, vector constante
# %x0, aproximaci�n inicial 
# %tol, tolerancia
# %Nmax, n�mero m�ximo de iteraciones

# %Salidas
# %x, soluci�n
# %iter, n�mero de iteraciones
# %err, error

# Método iterativo Jacobbi Matriz de coeficientes de entrada A, matriz de valores b, número de iteración n, error c (la matriz de lista es la preferida por la matriz de simulación de lista)

def Jacobi(A,b,n=100,c=0.0001, x = None):
    n=int(input("Max iterations "))
    c=float(input("Tolerance "))
    nx = []
    count = 0 #Cuenta el número de iteraciones
    lc = []
    if len (A) == len (b): #Si A y b tienen la misma longitud, comience la iteración; de lo contrario, la ecuación no tiene solución
        if(x == None):
            x = [] # Valor inicial iterativo inicializado en una sola fila toda la matriz 0
            for i in range(len(b)):
                x.append([0])
        count = 0 #Cuenta el número de iteraciones
        while count < n:
            nx = [] # Guardar el conjunto de valores después de una sola iteración
            print(f'iter : {count}\n x: {x}\n lc : {lc}\n -----------------------------')
            for i in range(len(x)):
                nxi = b[i][0]
                for j in range(len(A[i])):
                    if j!=i:
                        nxi = nxi+((-A[i][j])*x[j][0])
                nxi = nxi/A[i][i]
                nx.append ([nxi]) # Calculado iterativamente el siguiente valor xi
            lc = [] # almacena el conjunto de errores entre los resultados de dos iteraciones
            for i in range(len(x)):
                lc.append(abs(x[i][0]-nx[i][0]))
            if max(lc) < c:
                break #Cuando eumplel error c con los requisitos, devuelve el resultado del cálculo
            x = nx
            count = count + 1
    else:
        return False
    print( nx,  count, max(lc))
    return nx,  count, max(lc)


