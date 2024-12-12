"""""
Escribir un programa que pregunte el correo electrónico del usuario en la consola y muestre por pantalla otro
correo electrónico con el mismo nombre (la parte delante de la arroba @) pero con dominio ceu.es.

"""""

correo = input("Introduce tu correo electrónico: ")


nombre = correo.split('@')[0]


nuevo_correo = nombre + "@ceu.es"

print(f"Tu nuevo correo electrónico es: {nuevo_correo}")



# Se usa el método .split('@'), que divide la cadena en dos partes:
# [0]: La parte antes de la arroba (el nombre).
# [1]: La parte después de la arroba (el dominio actual).