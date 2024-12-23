"""""

La empresa Apper necesita una aplicación que le permita
llevar el registro de los empleados que trabajan en su planta.
Realizar un algoritmo que pida el número de empleados de la
empresa, Número de legajo, Apellido y nombre, Edad, Sueldo
y Puesto que ocupa. La codificación de los puestos seria :
SUPERVISOR ’S’- GERENTE ‘G’ - PLANTA ‘P’
El programa al final debe de mostrar los siguientes resultados:
a. Cantidad de empleados por puesto.
b. Empleados Mayores de 40 Años.
c. Apellido y nro de legajo de los empleados que ganan
más de $200.000

"""""
cantidad_de_supervisores = 0
cantidad_de_gerentes = 0
cantidad_de_planta = 0

empleados_mayores_40 = []

emplados_sueldo_mas_200 = []


num_emplados = int(input("Ingrese el número de empleados de su empresa: "))

for i in range(num_emplados):
    print(f"Ingrese los datos del empleado {i + 1}: ")
    legajo = int(input("Número de legajo: "))
    nombre_apellido = input("Apellido y Nombre: ")
    edad = int(input("Ingrese su edad: "))
    sueldo = float(input("Ingrese su sueldo: "))
    puesto = input("Ingrese su puesto (S - G - P): ")

    if puesto == "S":
      cantidad_de_supervisores += 1
    elif puesto == "G":
       cantidad_de_gerentes += 1
    elif puesto == "P":
       cantidad_de_planta += 1
   


    if edad > 40:
       empleados_mayores_40.append(f"{nombre_apellido} Legajo: {legajo}")
   
    if sueldo > 200000:
      emplados_sueldo_mas_200.append(f"{nombre_apellido} Legajo: {legajo}")

print(f"Cantidad de supervisores: {cantidad_de_supervisores}")

print(f"Cantidad de gerentes: {cantidad_de_gerentes}")

print(f"Cantidad de trabajadores en planta: {cantidad_de_planta}")

print("Listado de los empleados mayores a 40.")

print(empleados_mayores_40)

print("Listado de los empleados con sueldo mayor a $200.000 mil. ")

print(emplados_sueldo_mas_200)
