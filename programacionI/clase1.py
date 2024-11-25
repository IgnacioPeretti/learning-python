"""""
Sean N y M dos números naturales, escriba un algoritmo para determinar si N es divisible por M
"""""


# Datos de entrada: Dos números naturales N & M


N = int(input("Ingrese el número N:"))
M = int(input("Ingrese el número M:"))


if M == 0:
    print("Error: No se puede dividir por cero.")
elif N % M == 0:
    print(f"El número {N} es divisible por el número {M}")
else:
    print(f"{N} no es divisible por {M}")


# Realizado con una función

def verificar_divisibilidad(N, M):
    if M == 0:
        print("Error: No se puede dividir por cero.")
    elif N % M == 0:
        print(f"El número {N} es divisible por el número {M}")
    else:
        print(f"{N} no es divisible por {M}")

N = int(input("Ingrese el valor de N: "))
M = int(input("Ingrese el valor de M: "))

verificar_divisibilidad(N, M)


"""""
Realizar un algoritmo que calcule el área de un triángulo. [base * altura / 2]

Entrada de datos:

Se solicitan los valores de la base y la altura del triángulo utilizando input().
Como los valores pueden ser decimales, los convertimos a tipo float para permitir ingresar números con decimales.
"""""


base = float(input("Ingrese la base:"))
altura = float(input("Ingrese la altura:"))
area = (base * altura)/2

print(f"El área de su triangulo es: {area} m23")



"""""
Realizar un algoritmo que permita ingresar por teclado:
nombre, apellido, edad y domicilio y muestre los datos por pantalla solamente si se ingresaron.

Datos de entrada: Nombre, Apellido, Edad, Domicilio cada una guardada en sus respectivas variables.
Se ingresa por input cada una de ellas y se muestra luego con un print, el if verifica si todas las variables tienen algún valor.
"""""

nombre = input("Ingrese su nombre:")
apellido = input ("Ingrese su apellido:")
edad = input("Ingrese su edad:")
domicilio = input("Ingrese su domicilio:")

if nombre and apellido and edad and domicilio:
    print(f"Su nombre es {nombre} {apellido}, tiene {edad} años de edad y su domicilio es {domicilio}")
else:
    print("Error: Debe completar todos los campos")



"""
En la siguiente tabla se muestran las categorías a las que pertenecen los signos del zodíaco.
Se quiere diseñar el algoritmo de un programa que:
1. Muestre el listado de los signos del zodíaco, con sus números asociados.
2. Pida por teclado un número (dato entero) asociado a un signo del zodíaco.
3. Muestre la categoría a la que pertenece el signo del zodíaco seleccionado.

"""


signos = dict
{
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
    12:"Pscis"
}

print(signos)




