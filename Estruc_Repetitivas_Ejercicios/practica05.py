"""""
Escribir un programa que pida al usuario un numero entero y muestre por pantalla un triangulo rectangulo como el de mas
abajo, de altura el numero introducido.

*
**
***
****
*****
"""""



altura = int(input("Ingrese la altura de el triangulo: "))
area = 1
for i in range(1, altura + 1):
    print("*" * i)