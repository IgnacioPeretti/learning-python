"""""
Hacer un programa que pida un número por teclado y
guarde en una lista su tabla de multiplicar hasta
el 10.
"""""


numero = int(input("Ingrese un número: "))

lista = []

for i in range(1,11):
    lista.append(i*numero)


print(f"Tabla de multiplicar del número {numero}: {lista}")