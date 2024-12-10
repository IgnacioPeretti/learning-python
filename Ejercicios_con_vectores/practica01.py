"""""
Realizar un algoritmo que permita el ingreso por teclado de los 30
elementos de un vector numérico, duplicar sus valores y luego
imprimirlos en el orden ingresado
"""""

vector = []

print("Ingrese 30 números:")
for i in range(30):
    numero = float(input(f"Ingrese el número {i + 1}: "))
    vector.append(numero)

# Duplicar los valores de los elementos
vector_duplicado = [x * 2 for x in vector]

print("\nValores duplicados:")
for valor in vector_duplicado:
    print(valor)
