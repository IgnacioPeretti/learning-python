"""""
Dado un arreglo con N elementos, genere otro sin elementos repetidos
"""""

vector = [1,1,3,3,4,4,4,5,7,8,8]

arreglo_sin_repetidos = []

for elemento in vector:
    if elemento not in arreglo_sin_repetidos:
        arreglo_sin_repetidos.append(elemento)


print(f"El arreglo original es: {vector}")
print(f"Arreglo sin elementos repetidos: {arreglo_sin_repetidos}")