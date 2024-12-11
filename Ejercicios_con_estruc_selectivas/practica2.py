"""""
Realizar un algoritmo que pida por teclado dos valores que serán almacenados en las variables v1 y v2.
Luego intercambie los valores de las variables. Mostrar los valores de las variables por pantalla.
"""""


v1 = input("Ingrese el valor de la variable 1:")

v2 = input("Ingrese el valor de la variable 2:")

v1, v2 = v2, v1

print(f"El valor de la variable 1 es: {v1}")
print(f"El valor de la variable 2 es: {v2}")

