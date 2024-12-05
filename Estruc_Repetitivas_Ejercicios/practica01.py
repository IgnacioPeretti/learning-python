"""""
La universidad tomará examenes grupales de 5 personas y los alumnos pueden elegir armar
el grupo libremente entre sus compañeros pero el promedio de edad del grupo determinara
que enunciado deben realizar.

si la edad promedio esta entre 18 y 20  realizaran el enunciado 1.
si la edad promedio esta entre 20 y 30  realizaran el enunciado 2.
si la edad promedio es mayor a 30  realizaran el enunciado 3.
"""""

print("TRABAJO GRUPAL")

total_edades = 0
num_integrantes = 5

for i in range (5):
    edades = int(input(f"Ingrese la edad del integrante {i+1}: "))
    total_edades += edades

print(total_edades)

promedio_edades = total_edades / num_integrantes

print(f"El promedio de edad del grupo es: {promedio_edades}")

if 18 <= promedio_edades < 20:
    print("El grupo realizará el enunciado 1.")
elif 20 <= promedio_edades < 30:
    print("El grupo realizará el enunciado 2.")
elif promedio_edades >= 30:
    print("El grupo realizará el enunciado 3.")
else:
    print("El grupo no cumple con los requisitos de edad.")




