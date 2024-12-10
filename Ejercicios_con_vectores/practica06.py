"""""
Debes recorrer un array con números decimales y al finalizar mostrar por pantalla los siguientes datos
- El número mayor encontrado en el array
- El número menor encontrado en el array
- El valor promedio de entre los números de todo el array

"""""

vector = [12.5, 1.2, 3.3, 15.5, 8.8]

suma = 0
mayor = vector[0]
menor = vector[0]


for elemento in vector:
    suma += elemento
    if elemento > mayor:
        mayor = elemento
    if elemento < menor:
        menor = elemento

promedio = suma / len(vector)    


print(f" 1- El número mas grande de este vector es: {mayor}")


print(f" 2- El número mas chico de este vector es: {menor}")

    
print(f" 3- El valor promedio entre los números es: {promedio} ")