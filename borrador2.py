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