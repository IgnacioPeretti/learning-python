"""""
Escriba un algoritmo que multiplique dos
vectores. Los vectores deben tener la
misma cantidad de elementos, mostrar el
tercer vector con la multiplicaciones
correspondientes

"""""


def cargar_vector(vector, nombre):
    for i in range(longitud):
            vector[i] = int(input(f"Ingrese los elementos del {nombre}: "))




longitud = int(input("Ingrese la longitud del vector: "))


vector1 = [None] * longitud
vector2 = [None] * longitud
vector3 = [None] * longitud

cargar_vector(vector1, "Vector1")
cargar_vector(vector2, "Vector2")

for i in range(longitud):
      vector3[i] = vector1[i] * vector2[i]


print(f"El resultado final es: {vector3}")






    

