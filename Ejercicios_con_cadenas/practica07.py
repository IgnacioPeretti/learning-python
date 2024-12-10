"""""
Escribir un programa que pregunte al usuario la fecha de su nacimiento en formato dd/mm/aaaa y muestra
por pantalla, el día, el mes y el año. Adaptar el programa anterior para que también funcione cuando el día o
el mes se introduzcan con un solo carácter.

"""""

fecha_de_nacimiento = input("Ingrese su fecha de nacimiento en formato dd/mm/aa :  ")

dia = fecha_de_nacimiento.split("/")[0]

mes = fecha_de_nacimiento.split("/")[1]

año = fecha_de_nacimiento.split("/")[2]

print(f"Su fecha de nacimiento es el día {dia} del mes {mes} del año {año}.")