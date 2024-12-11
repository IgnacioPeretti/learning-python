
"""""
Realizar un algoritmo que solicite la nota de un alumno (de 1 a 10), y en base a ella determine su
calificación:
• Si no llega a 6 = “Desaprobado”
• De 6 y menor a 8 = “Bueno”
• De 8 y menor a 10 = “Muy Bueno”
• 10 = “Excelente”
"""""


nota = int(input("Ingrese la nota de su examen:"))

if nota < 1 or nota > 10:
    print("Error: número incorrecto")
else:
    print(f"Su nota es: {nota}")


if nota >= 1 and nota < 6:
    print("Calificación: Desaprobado")
elif nota >= 6 and nota < 8:
    print("Calificación: Bueno")
elif nota >= 8 and nota < 10:
    print("Calificación: Muy bueno")
elif nota == 10:
    print("Calificación: Excelente")





