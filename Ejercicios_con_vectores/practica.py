"""
Cargar y mostrar un vector
Suma y promedio de los elementos de un vector
Buscar un número dentro del vector
Encontrar el valor máximo y mínimo
Ordenarlo de menor a mayor y viceversa
Invertir un vector
"""

n = int(input("Ingrese el tamaño del vector:"))

vector = []

for i in range(n):
    numero = int(input(f"Ingrese el elemento {i + 1}: "))
    vector.append(numero)

print(vector)

suma = sum(vector)

promedio = suma // len(vector)

print(f"La suma del vector es: {suma}")

print(f"El promedio de los numeros de el vector es: {promedio}")


encontrar = int(input("Ingrese el número que quiere encontrar: "))



if encontrar in vector:
        print(f"El número {encontrar} esta en el vector")
elif encontrar not in vector:
        print("El número no esta en el vector.")


maximo = max(vector)
minimo = min(vector)

print(f"El número maximo del vector es {maximo}")
print(f"El número minimio del vector es {minimo}")


vector.sort()  
print("Vector ordenado ascendente:", vector)

vector.sort(reverse=True)  
print("Vector ordenado descendente:", vector)


vector_invertido = vector[::-1]  

print("Vector invertido:", vector_invertido)