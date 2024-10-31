# Variables

"""""
Una variable es un espacio de almacenamiento que se utiliza para guardar datos, 
permitiendo que estos sean referenciados y manipulados a lo largo del programa. 
Se le asigna un nombre y puede contener diferentes tipos de valores, como números, cadenas o listas.
(INT, FLOAT, BOOLEAN, STRING)

"""""


my_variable = " Me llamo ignacio "

print(my_variable)

my_age_variable2 = 24

print(my_age_variable2)

my_bool_variable = False

print(my_bool_variable)

my_int_to_str_variable = str(my_age_variable2)
print(my_int_to_str_variable)
print(type(my_int_to_str_variable))


# Concatenación de variables en un print

print(my_variable, my_age_variable2, my_bool_variable, my_int_to_str_variable)



# Funciones del sistema

print(len(my_variable))

print("Este valor es de:", my_bool_variable)



# Variables en una sola línea, Aunque podamos hacerlo no es una muy buena práctica

name, surname, alias, age = "Ignacio", "Peretti", "Nacho", 24

print("Me llamo", name,", mi apellido es", surname,", me dicen", alias, "y tengo", age,"años de edad.")


# Inputs 

name = input(" ¿Cual es tu nombre? ")
age = input(" ¿Cuantos años tienes? ")

print(name)
print(age)


"""""
En Python, los tipos de variables más comunes son:

int: Números enteros (5, -3).
float: Números de punto flotante (3.14, -0.001).
str: Cadenas de texto ("Hola, mundo").
bool: Valores booleanos (True, False).
list: Listas, que pueden contener múltiples elementos ([1, 2, 3], ["a", "b", "c"]).
tuple: Tuplas, similares a las listas pero inmutables (1, 2, 3).
dict: Diccionarios, que almacenan pares clave-valor ({"nombre": "Juan", "edad": 30}).
set: Conjuntos, que almacenan elementos únicos ({1, 2, 3}).

"""""