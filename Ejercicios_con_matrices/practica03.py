"""""
Rellenar y recorrer una matriz.

Programa para un estadio de futbol que quiere calcular la potencia de los focos de sus luces,

se necesita calcular la potencia de las dos diagonales de la matriz 

ejemplo :

 {1, 2, 3
  4, 5, 6
  7, 8, 9}

desde el indice superior derecho al indice inferior izquiero 
y el indice superior izquierdo al derecho.

si llegan a compartir un valor en el medio, este se tiene que sumar solo una vez.

"""""

n = int(input("Ingrese el tamaño de la matriz (n): "))

matriz = []

for i in range(n):
  fila = []
  for j in range(n):
    elemento = int(input(f"Ingrese el elemento [{i}][{j}]: "))
    fila.append(elemento)
  matriz.append(fila)

print("Matriz ingresada: ")
for fila in matriz:

  print(fila)


diagonal_principal = 0
diagonal_secundaria = 0


for i in range(n):
  diagonal_principal += matriz[i][i]
  diagonal_secundaria += matriz[i][n - 1 - i]

if n % 2 == 1:
  print("La matriz es impar")
  elemento_central = matriz[n // 2][n // 2] # n//2 divide la matriz por la mitad, apuntando al índice central cuando el tamaño es impar.
  suma_total = diagonal_principal + diagonal_secundaria - elemento_central
else:
  print("La matriz es par")
  suma_total = diagonal_principal + diagonal_secundaria


print(f"La potencia total de las luces es: {suma_total}")