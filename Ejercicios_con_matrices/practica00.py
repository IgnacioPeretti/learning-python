"""""
Realizar un algoritmo que muestre  la tabla pitagórica
"""""

tabla = []

for k in range(10):
    tabla.append([0]*10)

for i in range(0, 10, 1):
    for k in range(0, 10, 1):
        tabla [i][k] = i*k

for i in range(0, 10, 1):
    print(tabla[i])


