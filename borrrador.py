n = int(input("Ingrese el tamaño de la matriz: "))

matriz = []
for i in range(n):
    fila = []
    for j in range(n):
        elemento = int(input(f"Ingrese el elemento [{i}] [{j}]:"))
        fila.append(elemento)
    matriz.append(fila)


print("MATRIZ INGRESADA.")

for fila in matriz:
    print(fila)


diagonal_principal = 0

diagonal_secundaria = 0

for i in range(n):
    diagonal_principal += matriz[i][i]
    diagonal_secundaria += matriz[i][n - 1 - i]

if n % 2 == 1:
    print("MATRIZ IMPAR.")
    elemento_central = matriz[n // 2][n // 2]
    suma_total = diagonal_principal + diagonal_secundaria - elemento_central
else:
    print("MATRIZ PAR.")
    suma_total = diagonal_principal + diagonal_secundaria


print(f"La potencia total de las luces es: {suma_total}")
