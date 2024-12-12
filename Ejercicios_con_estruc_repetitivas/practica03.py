"""""
Lea N número y halle la suma de ellos.
"""""



numero = int(input("Ingrese cuantos números quiere sumar: "))

suma = 0

for i in range(numero):
    num = int(input(f"Ingrese el número {i+1}: "))
    suma += num
    

print("La suma de todos los números es: ", suma )
    