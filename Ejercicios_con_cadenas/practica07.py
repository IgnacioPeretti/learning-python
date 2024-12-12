"""""
Escribir un programa que pregunte al usuario la fecha de su nacimiento en formato dd/mm/aaaa y muestra
por pantalla, el día, el mes y el año. Adaptar el programa anterior para que también funcione cuando el día o
el mes se introduzcan con un solo carácter.

"""""

fecha_de_nacimiento = input("Ingrese su fecha de nacimiento en formato dd/mm/aaaa: ")

dia, mes, año = fecha_de_nacimiento.split("/")

print(f"Su fecha de nacimiento es el día {int(dia)} del mes {int(mes)} del año {int(año)}.")
