lista1 = [2, 3, 4]
lista2 = [4, 1, 7]
resultados = []

for num1 in lista1:
    for num2 in lista2:
        if num1 > num2:
            resultados.append("El número {} de la primera lista es mayor que el número {} de la segunda lista.".format(num1, num2))
        elif num1 < num2:
            resultados.append("El número {} de la primera lista es menor que el número {} de la segunda lista.".format(num1, num2))
        else:
            resultados.append("Los números {} y {} son iguales.".format(num1, num2))

for resultado in resultados:
    print(resultado)
#pruebas