"""""
Comprobamos que un número sea positivo para calcular su raíz cuadrada
"""""
import math

numero = int(input("Ingrese un número:"))

while numero < 0:
    print("Debe ser un número positivo")
    numero = int(input("Ingrese un número:"))


print(f"Su raíz cuadrada es: {(math.sqrt(numero)):.2f}")