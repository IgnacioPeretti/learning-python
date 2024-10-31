# Variables

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




