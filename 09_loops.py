### Bucles ### 


"""""
Un bucle permite ejecutar un bloque de código de manera repetitiva mientras se cumpla una condición determinada. 
Los bucles pueden realizar tareas repetitivas de manera eficiente sin tener que escribir el mismo código varias veces.

Existen principalmente dos tipos de bucles en Python: For & While

for se usa cuando sabes cuántas veces necesitas ejecutar el bloque de código.
while se ejecuta mientras una condición especificada sea verdadera.
"""""



my_condition = 0

while my_condition < 10:          # El while esta atado a siempre cumplir una condición
    print(my_condition)
    my_condition += 1
else:
    print(10,"Mi condición es mayor o igual que 10")

print("la ejecución continúa")


while my_condition < 20:
    my_condition += 1
    if my_condition == 15:
        print(15,"Se detiene la ejecución")
        break

    print(my_condition)

print("la ejecución continúa")


my_list = [35, 23, 16, 19, 20, 20]

my_tuple = (35, 1.77, "Ignacio", "Ignacio", "Peretti")

my_set = {"ignacio", "peretti", 24}

my_dict = {"Nombre":"Ignacio", "Apellido":"Peretti", "Edad":24, 1:"Python"}


for element in my_list:     # Un for se repite tantas veces como elementos tengamos 
    print(element)

print("La ejecucion continua")

for element in my_tuple:     
    print(element)

print("La ejecucion continua")

for element in my_set:     
    print(element)

print("La ejecucion continua")

for element in my_dict.values():     
    print(element)

print("La ejecucion continua")

for element in my_dict:     
    print(element)
    if element == "Edad":
        break          # Cuando salimos de el bucle con un break salimos completamente de él


print("La ejecucion continua")

for element in my_dict:     
    print(element)
    if element == "Edad":
        continue   # continue vuelve al for sin ejecutar lo que esta debajo
    print("Se ejecuta")   
else:
    print("El bucle for para el diccionario a terminado")