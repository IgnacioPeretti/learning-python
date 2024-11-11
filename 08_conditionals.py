### Condicionales ###


my_condition = True

if my_condition:     # Es lo mismo que if my_condition == True:
    print("Se ejecuta la condición del if")

my_condition = 5 * 2

if my_condition == 11:
    print("Se ejecuta la condición del segundo if")


if my_condition == 10:
    print("Se ejecuta la condición del tercer if")


if my_condition > 10:
    print("El valor es mayor a 10")
else:
    print("El valor es menor o igual a 10")


my_condition = 11

if my_condition == 10:
    print("El valor es igual a 10")
elif my_condition > 10 and my_condition < 20:
    print("Es mayor a 10 y menor que 20")
elif my_condition == 1:
    print("El valor es igual a 1")
else:
    print("Es menor a 10 o mayor o igual a 20")

print("la ejecución continúa")


my_string = " Mi cadena de texto "

if my_string:
    print("My cadena de texto no esta vacía")

if my_string == " Mi cadena de textoooo ":
    print("Mis cadenas de texto coinciden")