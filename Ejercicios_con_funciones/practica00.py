"""""
Escriba una función que muestre si un númmero es primo o no.
"""""

def numprimo(numero):
    for i in range(2, numero):
        if (numero % 2 == 0):
            return False
    return True


numero = int(input("Ingrese un número para saber si es primo o no:"))


print(numprimo(numero))

