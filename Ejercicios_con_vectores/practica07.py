"""""
:Lea dos arreglos (A y B), y genere otro arreglo (C) con la combinación del primer y el segundo
arreglo de forma intercalada. El arreglo A y B pueden tener distintas cantidades de elementos.
Ejemplo:
a. Sea el arreglo A: 3, 2, 0
b. Sea el arreglo B: 7, 1, 8, 4, 5, 6
c. Generar el arreglo C: 3, 7, 2, 1, 0, 8, 4, 5, 6

"""""



arreglo_A = [3, 2, 0]
arreglo_B = [7, 1, 8, 4, 5, 6]

arreglo_C = []

longitud_maxima = max(len(arreglo_A), len(arreglo_B))

for i in range(longitud_maxima):
    if i < len(arreglo_A):  
        arreglo_C.append(arreglo_A[i])
    if i < len(arreglo_B):  
        arreglo_C.append(arreglo_B[i])

print("Arreglo intercalado C:", arreglo_C)
