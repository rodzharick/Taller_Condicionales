#programa para calcular en que cuadrante esta en un punto, de un plano cartesiano

#entrada
x= int(input("ingrese la coordenada x"))
y= int(input("ingrese la coordenada y"))

#proceso
if x==0:
    if y==0:
        print("estas en el origen del plano cartesiano(0,0) ")
    else:
        print("estas en el eje y")
elif y==0:
    print("estas en el eje ")
elif x>0:
    if y>0:
        print("estas en el cuadrante 1")
    else:
        print("estas en el cuadrante 4")
elif y<0:
    print("estas enel cuadrante 3")
else:
    print("estas en el cuadrante 2")

