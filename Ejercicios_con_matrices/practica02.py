"""""
Escriba un algoritmo que multiplique dos
vectores. Los vectores deben tener la
misma cantidad de elementos, mostrar el
tercer vector con la multiplicaciones
correspondientes

"""""
def cargar_vector(vec, nombre):
    for i in range(long):
        vec[i] = int(input(f"Ingrese el valor de {i + 1} para {nombre}: "))


long = int(input("Ingrese la longitud del vector: "))

vec1 = [None] * long
vec2 = [None] * long
vec3 = [None] * long

cargar_vector(vec1, "Vector1")
cargar_vector(vec2, "Vector2")


for i in range(long):
    vec3[i] = vec1[i] * vec2[i]


print(f"El resultado final es: {vec3}")




    

