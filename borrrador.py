n = 3
m = 3
matriz = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
]

# Sumar por filas
for i in range(n):
    suma_fila = sum(matriz[i])
    print(f"Suma de la fila {i}: {suma_fila}")

# Sumar por columnas
for j in range(m):
    suma_columna = sum(matriz[i][j] for i in range(n))
    print(f"Suma de la columna {j}: {suma_columna}")





# Buscar un número dentro de la matriz
n = 3
m = 3
matriz = [
    [10, 20, 30],
    [40, 50, 60],
    [70, 80, 90]
]

buscar = int(input("Ingrese el número a buscar: "))
encontrado = False

for i in range(n):
    for j in range(m):
        if matriz[i][j] == buscar:
            print(f"Número encontrado en la posición [{i}][{j}]")
            encontrado = True

if not encontrado:
    print("El número no está en la matriz.")



# Matriz invertida

n = 3
m = 3
matriz = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
]

matriz_transpuesta = [[matriz[j][i] for j in range(n)] for i in range(m)]

print("Matriz original:")
for fila in matriz:
    print(fila)

print("Matriz transpuesta:")
for fila in matriz_transpuesta:
    print(fila)