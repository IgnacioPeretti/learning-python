"""""
Solicitar al usuario que ingrese números enteros positivos y, por cada uno de ellos
imprimir la suma de los digitos que lo componen. La condición de corte es que se 
ingrese el número -1. Al finalizar, mostrar cuantos de los números ingresados por el
usuario son pares.
"""""


pares = 0

while True:
    n = int(input("Ingrese un número positivo o (-1) para salir: "))
    if n == -1:
        break
    if n < 0:
        print("Por favor, ingrese un número positivo.")
        continue

    if n % 2 == 0:
        pares += 1

    suma = 0
    numero = n
    while numero != 0:
        digito = numero % 10
        suma += digito
        numero = numero // 10

    print(f"Suma de los dígitos de {n}: {suma}")

print(f"Se ingresaron {pares} números pares.")
