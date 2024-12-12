"""""
Se quiere diseñar el algoritmo de un programa que:
1. Pida por teclado una fecha en tres variables: día, mes y año (datos enteros).
2. Muestre por pantalla:

• “FECHA CORRECTA”, en el caso de que la fecha sea válida.
• “FECHA INCORRECTA”, en el caso de que la fecha no sea válida.

Nota1:

Para que una fecha sea válida, se tiene que cumplir que:
• El mes debe ser mayor o igual que 1 y menor o igual que 12.
• El día debe ser mayor o igual que 1 y menor o igual que un número, el cual dependerá del mes y año introducidos por el usuario.

Nota2: Hay que tener en cuenta que:

• Tienen 31 días: enero, marzo, mayo, julio, agosto, octubre y diciembre.
• Tienen 30 días: abril, junio, septiembre y noviembre.
• Tiene 29 días: febrero (si el año es bisiesto).
• Tiene 28 días: febrero (si el año no es bisiesto).

Nota3:

Son bisiestos todos los años múltiplos de 4, excepto aquellos que son múltiplos de 100 pero no
de 400.

"""""

dia = int(input("Ingrese el día de la fecha: "))
mes = int(input("Ingrese el mes de la fecha: "))
año = int(input("Ingrese el año de la fecha: "))

print(f"Su fecha es: {dia}/{mes}/{año}")


# Verificación de mes válido

if mes < 1 and mes > 12:
    print("Fecha Incorrecta: El mes no es válido")
else:
    # Determinar si el año es bisiesto

    if (año % 4 == 0 and año % 100 != 0) or (año % 400 == 0):
        bisiesto = True
    else:
        bisiesto = False


# Días válidos para cada mes

if mes == 1 or mes == 3 or mes == 5 or mes == 7 or mes == 8 or mes == 10 or mes == 12:
    max_dia = 31
elif mes == 4 or mes == 6 or mes == 9 or mes == 11:
    max_dia = 30
elif mes == 2:
    if bisiesto:
        max_dia = 29
    else:
        max_dia = 28


# Verificar si el día es válido

if dia < 1 or dia > max_dia:
        print("Fecha Incorrecta: El día no es válido para este mes.")
else:
    print("Fecha Correcta")
    




