"""""
Escribir un programa que almacene la cadena de caracteres contraseña en una variable,
pregunte al usuario por la contraseña e imprima por pantalla si la contraseña introducida por
el usuario coincide con la guardada en la variable sin tener en cuenta mayúsculas y
minúsculas.

"""""


variable1 = "contraseña"


pedir_contraseña = input("Ingrese la contraseña:")

if pedir_contraseña == variable1:
    print("La contraseña es correcta.")
else:
    print("Contraseña incorrecta.")