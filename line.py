def line():
    print("TO DO")
coeficiente_A = float(input("Ingrese el coeficiente A: "))
coeficiente_B = float(input("Ingrese el coeficiente B: "))
coeficiente_X1 = float(input("Ingrese el coeficiente X1: "))
coeficiente_X2 = float(input("Ingrese el coeficiente X2: "))
resultado_1 = coeficiente_A
print("El coeficiente A de su ecuación de la recta es: ", resultado_1)
resultado_2 = coeficiente_B
print("El coeficiente de su ecuación de la recta es: ", resultado_2)
resultado_3 = coeficiente_X1 
print("El coeficiente de su ecuación de la recta es: ", resultado_3) 
resultado_4 = coeficiente_X2
print("El coeficiente de su ecuación de la resta es: ", resultado_4)

print("Dados los siguientes valores:")
Y1 = float((coeficiente_A * coeficiente_X1) + coeficiente_B)
resultado_1 = Y1
print(resultado_1)
Y2 = float((coeficiente_A * coeficiente_X2) + coeficiente_B)
resultado_2 = Y2
print(resultado_2)

print("Dados los siguientes puntos:")
P1 = (coeficiente_X1, Y1)
resultado_3 = P1
print(resultado_3) 
P2 = (coeficiente_X2, Y2)
resultado_4 = P2
print(resultado_4)

print("Cálculo de distancia: ")
calculo_1 = float(coeficiente_X2 - coeficiente_X1)
calculo_2 = float(Y2 - Y1)
exponente_1 = 2
calculo_3 = float(calculo_1** exponente_1)
calculo_4 = float(calculo_2** exponente_1)
calculo_5 = float(calculo_3 + calculo_4)
exponente_2 = 0.5
resultado_5 = float(calculo_5** exponente_2)
print("La distancia entre ellos es: ", resultado_5) 
