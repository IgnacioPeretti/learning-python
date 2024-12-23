"""""
Escriba un algoritmo que multiplique dos vectores. Los vectores deben tener la
misma cantidad de elementos, mostrar el tercer vector con la multiplicaciones
correspondientes
"""""
tamaño = int(input("Ingrese cuantos numeros quiere agregar al vector: "))

vector1 = [None] * tamaño   
vector2 = [None] * tamaño
vector3 = [None] * tamaño

print("Vector 1")
for i in range(tamaño):
   vector1[i] = int(input(f"Ingrese el elemento {i + 1}: "))

print("Vector 2")
for i in range(tamaño):
   vector2[i] = int(input(f"Ingrese el elemento {i + 1}: "))


print(f"Vector 1: {vector1}, Vector 2: {vector2}")

for i in range(tamaño):
   vector3[i] = vector1[i] * vector2[i]

print("El resultado final es")
print(f"Vector 3: {vector3}")






    

