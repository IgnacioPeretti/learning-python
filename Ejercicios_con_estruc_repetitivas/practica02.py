"""""
Lea N número y halle el menor de ellos.
"""""

numero = int(input("Ingresa la cantidad de números: "))

menor = float("inf")


for i in range(numero):
    num = float(input(f"Ingrese el valor de N{i+1}:  "))


    if num < menor:
        menor = num

print("El menor de los numeros es:", menor)
    