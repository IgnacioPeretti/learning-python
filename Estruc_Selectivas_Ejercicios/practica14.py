


miCadena = "HOLA NACHO"

longitud = len(miCadena)

print("La longitud de mi cadena es:", longitud)


print(miCadena[2])

print(miCadena[0:10:2])

print(miCadena[::-1])


subcadena = "NACHO"

print(subcadena + miCadena)
print(subcadena in miCadena)

cadena = "Bienvenidos a la universidad."

print(cadena.split())

texto = "manzana,banana,cereza"
resultado = texto.split(",")
print(resultado)




nombre = str(input("¿Como te llamas?: "))


print(nombre.upper() + " tiene " + str(len(nombre)) + " letras")
