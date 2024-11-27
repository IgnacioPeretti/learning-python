"""""
Para tributar un determinado impuesto se debe ser mayor de 16 años y tener unos ingresos
iguales o superiores a 1000 € mensuales. Escribir un programa que pregunte al usuario su
edad y sus ingresos mensuales y muestre por pantalla si el usuario tiene que tributar o no
"""""


edad = int(input("Ingrese su edad: "))

if edad >= 16:
    print("Usted puede tributar el impuesto")
else:
    print("Usted no puede tributar el impuesto")


ingresos = int(input("Ingrese sus ingresos mensuales: "))

if ingresos >= 1000:
    print("Usted debe tributar sus impuestos.")
else:
    print("Usted no debe tributar sus impuestos.")