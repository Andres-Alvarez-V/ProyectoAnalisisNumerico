

# Documentation

![Alt text](Images\MetodosNumerico.png?raw=true "Optional Title")


## Numerical solution of nonlinear equations.

### Incremental searches.
Given f (x) = 0, we apply the following steps:

- The continuity of f must be guaranteed with arguments
theoretical.
- We choose a starting value x0 and a Δx that expresses the
size of the interval that we want to find.
- We generate a sequence x0, x1, ..., xn such that
xn = xn − 1 + 4x.
- Each time a value of xn is generated, we find the value of f (xn).
- We observe the signs of f (xn) and f (xn − 1).
- We suspend the process when there is a change of
sign at f (xn) and f (xn − 1) or when we reach a limit of
iterations without finding said change.

```bash
read f, x0, Δx, IterMax 

xant <- x0
fant <- f(xant)
xact <- xant+Δx
fact <- f(xact)
ite <- 0

while fant*fact > 0 and IterMax > ite do
	xant <- xact
    fant <- fact
    xact <- xant+h
    fact <- f(xact)
end while

if fi*ff<0 then
    Entre xi,xf hay raiz
    
else if ff=0 then
    xf es raiz

else then
    No llegamos
    
end if 
``` 
        
### Bisection.
The method is quite simple, all it does is divide the
interval in the middle and check which side the root was to get a new interval.

```bash
read f, xi, xs, tol, niter 

fxi <- f(xi)
fxs <- f(xs)

if fxi == 0 then
	xi es raiz
else if fxs == 0 then
	xs es raiz
else if fxi*fxs<0 then
	xm <- (xi+xs)/2
	fxm <- f(xm)
    cont=1
    error=tol+1

    while error>tol and fxm != 0 and cont<niter do
        if fxi*fxm<0 then
            xs <- xm
            fxs <- fxm
        else then
            xi <- xm
            fxi <- fxm
        end if
        xaux <- xm
        xm <- (xi+xs)/2
        fxm <- f(xm)
        error <- abs(xm-xaux)
        cont <- cont + 1
	end while
    
    if fxm==0 then
		xm es raiz
    else if error<tol then
		xm es una aproximacion con tolerancia = tol
    else then
        fracaso en niter iteraciones
    end if
    
else then
	El intervalo es inadecuado
end if
``` 
        
### False rule.
It works the same as the bisection method, changing Only the method to select xm. In this case it is taken
a straight line from f (a) to f (b) and is taken as xm the value
where the x  intersects.

```bash
read f, xi, xs, tol, niter 

fxi <- f(xi)
fxs <- f(xs)

if fxi == 0 then
	xi es raiz
else if fxs == 0 then
	xs es raiz
else if fxi*fxs<0 then
	xm <- xi-((fxi*(xs-xi))/(fxs-fxi))
	fxm <- f(xm)
    cont <- 1
    error <- tol+1

    while error>tol and fxm != 0 and cont<niter do
        if fxi*fxm<0 then
            xs <- xm
            fxs <- fxm
        else:
            xi <- xm
            fxi <- fxm
        end if
        xaux <- xm
        xm <- (xi+xs)/2
        fxm <- f(xm)
        error <- abs(xm-xaux)
        cont <- cont + 1
	end while
    
    if fxm==0 then
		xm es raiz
    else if error<tol then
		xm es una aproximacion con tolerancia = tol
    else then
        fracaso en niter iteraciones
    end if
    
else then
	El intervalo es inadecuado
end if

``` 
        
### Fixed point.
The method is based on the idea of ​​converting f (x) = 0, into x = g (x)
somehow.

The fundamental idea of ​​the method is to arrive at a point where
satisfies the equality x = g (x) or we are close enough to
do it

```bash
read g, x0, tol, niter 

xant <- x0
e <- tol+1
cont <- 0


while tol < e and contador <= nmax do

	xact <- g(xant)
	e <- |xant - xact|
	contador <-  contador + 1
	xant <- xact

end while

if e > tol then
	no pudimos llegar a esa tolerancia con contador iteraciones
else then
	hubo contador iteraciones y la raiz se encuentra en xant con un error de e
end if
``` 
        
### Newton.
Let F ∈ C² [a, b] and Xv ∈ [a, b] such that F(xv) = 0 and F′(xv) != 0
then there exists d > 0 such that Newton's method generates a
sequence { Xn }∞ n = 0 that converges to Xv for any approximation
initial X0 ∈ [Xv − d, Xv + d].

```bash
read f, df, x0, tol, niter

fx <- f(x0)
dfx <- df(x0)
cont <- 0
error <- tol + 1

while error > tol and fx != 0 and cont < niter do
	x1 <- x0-(fx/dfx)
    fx <- f(x1)
    dfx <- df(x1)
    error <- |x1-x0|
    x0 <- x1
    cont <- cont + 1
end while

if fx==0 then
	x0 es raiz
else if error<tol then
    x1 es una aproximacion a una raiz con una tolerancia de: tol
else if dfx==0 then
	x1 es una posible raiz multiple
else then
	fracaso en niter iteraciones
end if            
``` 
        
### Secante.
In the secant method we take two values ​​of the function for
create the secant line to it and obtain a new value.
The logic behind this method is that it allows an approximation to the
Newton's method without the need to perform the derivative.

```bash
read f, x0, x1, tol, niter

fx0 <- f(x0)
fx1 <- f(x1)

if fx0 == 0 then
	x0 es raiz
else if fx1 == 0 then
	x1 es raiz
else then
    cont <- 1
    error <- tol + 1
    while error>tol and cont< niter do
        xaux <- x1 - (fx1*(x1 - x0)/(fx1 - fx0))
        faux <- f(xaux)
        error <- |xaux - x1|
        cont <- cont + 1
        x0 <- x1
        fx0 <- fx1
        x1 <- xaux
        fx1 <- faux
	end while
    if faux == 0 then
		xaux es raiz
    else if error < tol then
		xaux es una aproximacion con tolerancia = tol
    else then
		fracaso en niter iteraciones
	end if
end if
``` 
        
### Multiple roots.
Let F ∈ C^m [a, b]. The function has a multiplicity root m in Xv if and only if:

    0 = f (xv) = f ′ (xv) = f ′ ′ (xv) = ... = f (m − 1) (xv)

But f^(m) (xv) is different from zero.

```bash
read f, df, d2f, x0, tol, niter

xant <- x0
fant <- f(xant)
E <- tol + 1
cont <- 0

while E > tol and cont < niter do
    xact <- xant - fant*df(xant)/( ((df(xant))**2) - fant*d2f(xant)) 
    fact <- f(xact)
    E <- |xact - xant|
    cont <- cont + 1
    xant <- xact
    fant <- fact
end while

x <- xact
iter <- cont
err <- E

Resutado: x
Iteracio: iter
Error: err
``` 
        
## Solution of systems of linear equations.

### Gauss simple.
the general idea of ​​the method is to start from Ax = b to arrive at Ux = B where U is an upper triangular matrix.

```bash
read A, b

AB = concatenateMatrix(A,b)
n_rows <- AB.size()
m_columns <- AB[0].size()

for i <- 0 To n_rows-1
	pivote <- AB[i][i]
	for k <- i+1 To n_rows
		factor <- AB[i][k]/pivote
		for j <- 0 To m_columns
			AB[k][j] <- AB[k][j] - AB[i][j]*factor
		endFor
	endFor
endFor

ultfila <- n_rows-1
ultcolumna <- m_columns-1
X = matrixOfZeros(n_rows)

for i <- ultfila To -1 step -1
	suma <- 0
	for j <- i+1 To ultcolumna
		suma <- suma + AB[i][j]*X[j]
	endFor
	b <- AB[i][ultColumna]
	X[i] <- (b-suma)/AB[i][i]
endFor

X = matrixTranspose(X)

OUTPUT("Matrix Resultante AB: ")
OUTPUT(AB)
OUTPUT("Solucion: ")
OUTPUT(X)

``` 
        
### Gauss partial pivot.
In each stage k it is sought that akk (or the pivot) is of greater possible magnitude (absolute value) compared to others
values ​​in column k that are below akk.

```bash
read A, b

AB = concatenateMatrix(A,b)
n_rows <- AB.size()
m_columns <- AB[0].size()

for i <- 0 To n-1
	columna <- abs(AB[i][i])
	tempMax <- 0
	tempMaxIndex <- 0
	
	for j <- i To n
		if AB[j][i] > tempMax then
			tempMax <- AB[i][j]
			tempMaxIndex <- j
		endIf
	endFor
	
	if tempMaxIndex != 0 then
		temporal <- AB[i]
		AB[i] <- AB[tempMaxIndex]
		AB[tempMaxIndex] <- temporal
	endIf
endFor

for i <- 0 To n_rows-1
	pivote <- AB[i][i]
	for k <- i+1 To n_rows
		factor <- AB[i][k]/pivote
		for j <- 0 To m_columns
			AB[k][j] <- AB[k][j] - AB[i][j]*factor
		endFor
	endFor
endFor


ultfila <- n_rows-1
ultcolumna <- m_columns-1
X = matrixOfZeros(n_rows)

for i <- ultfila To -1 step -1
	suma <- 0
	for j <- i+1 To ultcolumna
		suma <- suma + AB[i][j]*X[j]
	endFor
	b <- AB[i][ultColumna]
	X[i] <- (b-suma)/AB[i][i]
endFor

X = matrixTranspose(X)

OUTPUT("Matrix Resultante AB: ")
OUTPUT(AB)
OUTPUT("Solucion: ")
OUTPUT(X)

```   

### factoring LU
If we can carry out Gaussian elimination in the system Ax = b
without row exchanges and such that the resulting elements
on the diagonal are different from 0, then we can factor the
matrix A in the product of a lower triangular matrix L and a
upper triangular matrix U (A = LU). Where L, U are arranged
as stated before.

```bash
read A, b

n <- A.size()
L <- identityMatrix(n)
U <- matrixOfZeros(n)
M <- A

for i <- 0 To n-1
	for j <- i+1 To n
		if M[j][i] != 0 then
			L[j][i] <- M[j][i]/M[i][i]
			M[j,i:n] <- M[j,i:n]-(M[j,i]/M[i,i])*M[i,i:n]
		endIf
	endFor
	U[i,i:n] <- M[i,i:n];
    U[i+1,i+1:n] <- M[i+1,i+1:n]
endFor

U[n-1,n-1] <- M[n-1,n-1]

L <- augmentedMatrix (L,b)
z <- sustprgr(L)
U <- augmentedMatrix (U,z)
x <- sustregr(U)
OUTPUT(x)
``` 
### factoring LU partial pivot
Suppose that the system Ax = b can be solved using
Gaussian elimination with partial pivoting. So there is a permutation matrix P such that the product PA can be
factored as the product of a lower triangular matrix L and
an upper triangular matrix U. That is,

PA = LU

The matrix L is constructed based on the multipliers located
according to their respective indices and with 1s on the diagonal, and the matrix U
is the matrix resulting from elimination. The final system is:

LUx = Pb

```bash
read A, b

n <- A.size()
L <- identityMatrix(n)
U <- matrixOfZeros(n)
P <- identityMatrix(n)
M <- A


for i <- 0 To n-1
	[a,b] <- max(M[i:,i:n])
	if a[0] != i then
		M[[i,a[0]],:] <- M[[a[0],i],:]
        P[[i,a[0]],:] <- P[[a[0],i],:]
        if i > 0 then
        	L[[i,a[0]],0:i]=L[[a[0],i],0:i]
        endIf
	endIf
	
	for j <- i+1 To n
		if M[j,i] != 0 then
			L[j,i] <- M[j,i]/M[i,i]
            M[j,i:n] <- M[j,i:n]-(M[j,i]/M[i,i])*M[i,i:n]
		endIf
	endFor
	U[i,i:n] <- M[i,i:n];
    U[i+1,i+1:n] <- M[i+1,i+1:n]		
endFor

U[n-1,n-1] <- M[n-1,n-1]

L <- augmentedMatrix (L,b)
z <- sustprgr(L)
U <- augmentedMatrix (U,z)
x <-  sustregr(U)
OUTPUT(x)
``` 

        

### Jacobi.

Jacobi's method is an iterative method, used to solve systems of linear equations of the type Ax = b . The algorithm takes its name from the German mathematician Carl Gustav Jakob Jacobi. Jacobi's method consists of using formulas such as fixed-point iteration.

The basis of the method consists of constructing an iteratively defined convergent sequence. The limit of this sequence is precisely the solution of the system. For practical purposes, if the algorithm stops after a finite number of steps, an approximation to the value of x of the solution of the system is reached.

The sequence is constructed by decomposing the system matrix in the following form:
    A = D + R

where D, is a diagonal matrix and R, is the sum of a lower triangular matrix L and an upper triangular matrix U then R = L + U. 


```bash
read A, b, x, iter, tol
nx <- []
count <- 0
lc  <- []

if A.size() == b.size():

	if(x == None) then
		x <- []
		for i <- 0 To b.size()
			x.add([0])
		endFor
	endIf
	count <- 0
	
	while count < n do
	
		nx <- []
		for i <- 0 To x.size()
			nxi <- b[i][0]
			for j <- 0 To A[i].size()
				if j != i then
					nxi <- nxi+((-A[i][j])*x[j][0])
				endIf
			endFor
			nxi <- nxi/A[i][i]
            nx.append ([nxi])
		endFor
		
		lc <- []
		
		for i <- 0 To x.size():
            lc.append(abs(x[i][0]-nx[i][0]))
        endFor
        if max(lc) < c then
            break
        endIf
        x <- nx
        count <- count + 1
	endWhile
else then
	OUTPUT("A y b deben tener las mismas dimensiones para que exista una solucion unica")
endIf

err <- max(lc)
OUTPUT("sol: ")
OUTPUT(nx)
OUTPUT("iter : {count}")
OUTPUT("err : {err}")
``` 
        
### Gauss seidel.

In numerical analysis the Gauss-Seidel method is an iterative method used to solve systems of linear equations. The method is named after the German mathematicians Carl Friedrich Gauss and Philipp Ludwig von Seidel and is similar to Jacobi's method.

Although this method can be applied to any system of linear equations that produces a matrix (square, of course, since for there to be a unique solution, the system must have as many equations as unknowns) of coefficients with the elements of its diagonal non-zero, the convergence of the method is only guaranteed if the matrix is diagonally dominant or if it is symmetric and, at the same time, positive definite.

```bash
read A, b, x, iter, tol

n <- A.size()
m <- A[0].size()


X <- x
diferencia <- matrixOfOnes(n)
errado <- tol+1

itera <- 0

while not(errado<=tolera or itera>iteramax) do
	for i <- 0 To n
		suma <- 0
		for j <- 0 To m
			if(i != j) then
				suma <- suma - A[i][j]*X[j]
			endIf
		endFor
		
		nuevo <- (B[i]+suma)/A[i][i]
		diferencia[i] <- |nuevo-X[i]|
        X[i] <- nuevo
	endFor
	errado <- max(diferencia)
    itera <- itera + 1
endWhile

X <- matrixTranspose(X)
if (itera > iteramax) then
	X <- 0
endIf

OUTPUT("Respuesta: ")
OUTPUT(X)

``` 
        
## Interpolation.
      

### Vandermonde.
Vandermonde matrix is a matrix that presents a geometric progression in each row. This matrix is named after the French mathematician Alexandre-Théophile Vandermonde.

```bash
read X, Y

n <- X.size()
m <- A[0].size()
A <- matrixOfZeros(n,n)

for i <- 0 To n
	for j <- 0 To n
		A[i][j] <- X[i]**j
	endFor
endFor

inversa <- matrixInverse(A)

coef <- []

for i <- 0 To n
	contador <-
	for j <- 0 To n
		contador +=inversa[i][j]*Y[j]
	endFor
	coef.add(contador)
endFor

frase <- "el polinomio que representa esta funcion es "

for i <- 0 To coef.size()
	if i == 0 then
		frase <- frase + to_string(coef[i]) + "+"
	else if i == n-1 then
		frase <- frase + to_string(coef[i]) + "x^" + to_string(i)
	else then
		frase <- frase + to_string(coef[i]) + "x^" + to_string(i) + "+"
	endIf
endFor


OUTPUT(frase)
``` 

