"""""
Diseñar un programa que permita cargar un vector con 100 datos numéricos, luego ingresar un número X y
buscar e informar si X se encuentra en el vector y si se encuentra, cuántas veces aparece

"""""



import random

vector = [random.randint(1, 120) for i in range(100)]

print("Vector: ", vector)

n = int(input("Ingrese un número para buscar en el vector: "))

cantidad = vector.count(n)

if cantidad > 0:
    print(f"El número {n} se encuentra {cantidad} veces en el vector.")
else:
    print(f"El número {n} no se encuentra en el vector.")


