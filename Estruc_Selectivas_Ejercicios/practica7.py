"""""
Escribir un programa que pida al usuario dos números y muestre por pantalla su división. Si
el divisor es cero el programa debe mostrar un error
"""""


numero1 = int(input("Ingrese el primer número: "))

numero2 = int(input("Ingrese el segundo número: "))

if numero1 == 0 or numero2 == 0:
    print("ERROR: No se puede dividir por 0.")
else:
    division = (numero1 / numero2)
    print(division)





