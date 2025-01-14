"""""
Se dispone de una matriz de 12x7 elementos, donde las columnas representan días
de las semanas y las filas los meses del año, cada celda contiene el ingreso de
ventas que obtuvo el comercio según el día y mes especificado. Se pide la siguiente
información:
a. Calcular el total de ventas.
b. Calcular las ventas por meses.

"""""

matriz = [[0 for _ in range(7)] for _ in range(12)]


dias_semana = ["Lunes", "Martes", "Miércoles", "Jueves", "Viernes", "Sábado", "Domingo"]
meses = [
    "Enero", "Febrero", "Marzo", "Abril", "Mayo", "Junio",
    "Julio", "Agosto", "Septiembre", "Octubre", "Noviembre", "Diciembre"
    ]

for fila in matriz:
    print(fila)

import random

for i in range(12):
    for j in range(7):
        matriz[i][j] = random.randint(100, 1000)



print("Ventas de cada día en pesos:")

print(" ", " ".join(dias_semana))

for i, fila in enumerate(matriz):
    print(f"{meses[i]:<9} {fila}")



# Total de ventas


print("\nTotal de ventas por mes:")
for i, fila in enumerate(matriz):
    total_mes = sum(fila)
    print(f"{meses[i]:<9} {total_mes}")


# Total de ventas


# Calcular el total de ventas
total_ventas = sum(sum(fila) for fila in matriz)

print(f"\nEl total de ventas en todo el año es: {total_ventas} pesos")
