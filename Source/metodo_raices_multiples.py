# Este programa halla la solución a la ecuación f(x)=0 usando el método de raíces múltiples

# Entradas: 
# f, función continua -> f0
# f', función continua -> f1
# f'', función continua -> f2
# x0, aproximación inicial 
# tol, tolerancia
# Nmax, número máximo de iteraciones

# Salidas
# x, solución
# iter, número de iteraciones
# err, error
def raices_multiples(fun,df,d2f):
    x0 = float(input("Aproximacion inicial x0: "))
    tol = float(input("Tolerancia: "))
    nmax = int(input("Numero de iteracciones maximas: "))


    xant = x0
    fant = fun(xant)
    E = 1000
    cont = 0

    while(E > tol and cont < nmax):
        xact = xant - fant*df(xant)/( ((df(xant))**2) - fant*d2f(xant)) 
        fact = fun(xact)
        E = abs(xact - xant)
        cont += 1
        xant = xact
        fant =fact
    x = xact
    iter = cont
    err = E

    print(f"Resutado -> {x} \nIteracio: {iter}\nError: {err}")
