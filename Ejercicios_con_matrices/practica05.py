"""""
Suma de dos matrices: Escribe un programa que tome dos matrices de igual tamaño y calcule su suma.
"""""


n = int(input("Ingrese el número de filas de las matrices: "))
m = int(input("Ingrese el número de columnas de las matrices: "))

matriz1 = []
matriz2 = []



for i in range(n):
    fila = []
    for j in range(m):
        elemento = int(input(f"Ingrese el elemento [{i}][{j}]: "))
        fila.append(elemento)
    matriz1.append(fila)



print("Ingrese los datos de la segunda matriz.")


for i in range(n):
    fila = []
    for j in range(m):
        elemento = int(input(f"Ingrese el elemento [{i}][{j}]: "))
        fila.append(elemento)
    matriz2.append(fila)



print("La suma de las dos matrices es:")

resultado = []
for i in range(n):
   fila = []
   for j in range(m):
       suma = matriz1[i][j] + matriz2[i][j]
       fila.append(suma)
   resultado.append(fila)



print("La matriz 1 es: ")

for fila in matriz1:
    print(fila)

print("La matriz 2 es: ")

for fila in matriz2:
    print(fila)


print("El resultado de la suma es:")

for fila in resultado:
    print(fila)