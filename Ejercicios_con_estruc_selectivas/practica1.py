
"""
En la siguiente tabla se muestran las categorías a las que pertenecen los signos del zodíaco.
Se quiere diseñar el algoritmo de un programa que:
1. Muestre el listado de los signos del zodíaco, con sus números asociados.
2. Pida por teclado un número (dato entero) asociado a un signo del zodíaco.
3. Muestre la categoría a la que pertenece el signo del zodíaco seleccionado.

"""

signos = {

    1:"Aries",
    2:"Tauro",
    3:"Geminis",
    4:"Cáncer",
    5:"Leo",
    6:"Virgo",
    7:"Libra",
    8:"Escorpio",
    9:"Sagitario",
    10:"Capricornio",
    11:"Acuario",
    12:"Piscis"
}

print(f"A continuación podrás ver los signos: \n{signos}")


numero = int(input("Ingrese un número entre 1 y 12 para ver la categoría de su signo:"))

if numero < 1 or numero > 12:
    print("Error: Número incorrecto")
else:    
    print(f"Su signo es: {signos[numero]}")


if numero == 1 or numero == 5 or numero == 9:
    print("Categoría Fuego")
elif numero == 2 or numero == 6 or numero == 10:
    print("Categoría Tierra")
elif numero == 3 or numero == 7 or numero == 11:
    print("Categoría Aire")
elif numero == 4 or numero == 8 or numero == 12:
    print("Categoría Agua")
else:
    print("Vuelva a ingresar un número.")




