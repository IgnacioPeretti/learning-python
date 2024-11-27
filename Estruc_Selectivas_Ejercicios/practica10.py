"""""
Los alumnos de un curso se han dividido en dos grupos A y B de acuerdo al sexo y el
nombre. El grupo A esta formado por las mujeres con un nombre anterior a la M y los
hombres con un nombre posterior a la N y el grupo B por el resto. Escribir un programa que
pregunte al usuario su nombre y sexo, y muestre por pantalla el grupo que le corresponde.

"""""

# Pedimos el nombre y el sexo del usuario
nombre = input("Ingrese su nombre: ").strip()
sexo = input("Ingrese su sexo (M/H): ").strip().upper()


if sexo == "M":  # Mujer
    if nombre[0] < 'M':  
        print("Grupo A")
    else:  
        print("Grupo B")
elif sexo == "H":  # Hombre
    if nombre[0] > 'N':  
        print("Grupo A")
    else: 
        print("Grupo B")
else:
    print("Sexo no válido")

