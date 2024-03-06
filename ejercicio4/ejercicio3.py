# programa para saber tu estatura y tu peso tu estado de acuerdo al IMC

# input
PESO= int(input(" por favor ingrese su peso : "))
ALTURA= float(input(" por favor ingrese su altura : "))

#processing 
IMC = PESO/ALTURA**2

if IMC < 16:
    RESULTADO = "criterio de ingreso en hospital"
elif IMC <=17:
    RESULTADO = "infrapeso "
elif IMC <=18:
    RESULTADO = "bajo peso"
elif IMC <=25:
    RESULTADO = "peso normal (saludable)"
elif IMC <=30:
    RESULTADO = "sobrepeso (obesidaad tipo I)"
elif IMC <=30:
    RESULTADO = "sobrepeso cronico(obesidad de grado II) "
elif IMC <=35:
    RESULTADO = "obesidad premorbida(obesidad e grado III)"
elif IMC > 40:
    RESULTADO = "obesidad morbida(obesidad degrado IV)"

# output

print("si IMC es" ,IMC," y sus resultados son",RESULTADO,)