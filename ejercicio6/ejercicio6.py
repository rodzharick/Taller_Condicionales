from math import*
# programa para  Calcular e imprimir las raíces de la ecuación de segundo grado de coeficientes reales

#imput
A = int(input("porvafor ingrese el numero A :"))
B = int(input("porvafor ingrese el numero B :"))
C = int(input("porvafor ingrese el numero C :"))

#procesing
if A == 0:
    print( " No hay ecuacion cuadratica " )
else:
    D = B**2 -4*A*C
    if D == 0:
        X1 = -B /2*A
        X2 = X1
        print(" los resultados de la operacion son : ", X1, X2,)
    elif D > 0:
        x1 = (-B + sqrt(D))/2*A
        x2 = (-B - sqrt(D))/2*A
        print(" los resultado de las operaciones son : ", x1 , x2,)
    else:
        print( " no hay solucion real " )