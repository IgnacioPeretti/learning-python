"""""
Realizar un algoritmo que permita el ingreso por teclado de los 30
elementos de un vector numérico, duplicar sus valores y luego
imprimirlos en el orden ingresado
"""""

numero = [0] * 10

print(numero)


for i in range(len(numero)):
    numero[i] = int(input(f"Ingrese el elemento {i + 1}:"))


print(numero)

for i in range(len(numero)):
    print(f"El valor {i + 1} duplicado su valor es: {numero[i] * 2}.")