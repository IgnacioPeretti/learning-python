### Estructura de datos ###
### Diccionarios ###

"""""
Un diccionario es una estructura de datos que permite almacenar un conjunto de elementos en pares de clave-valor. 
Cada clave es única dentro del diccionario, y se utiliza para acceder al valor asociado a ella.

"""""


my_dict = dict()
my_other_dict = {}

print(type(my_dict))
print(type(my_other_dict))


my_other_dict = {"Nombre":"Ignacio", "Apellido":"Peretti", "Edad":24, 1:"Python"}

print(my_other_dict)
print(type(my_other_dict))

my_dict = {
    "Nombre":"Ignacio ",
    "Apellido":"Peretti",
    "Edad":24,
    "Lenguajes":{"Python", "Swift", "JavaScript"},
    1:1.77
}

# Podemos ver que tenemos una estructura dentro de otra, en este caso tenemos un set dentro de un diccionario.

print(my_other_dict)    
print(my_dict)

print(len(my_other_dict))
print(len(my_dict))


print(my_dict["Nombre"])

my_dict["Nombre"] = "Nacho"
print(my_dict["Nombre"])
print(my_dict)


my_dict["Ciudad"] = "Argentina"   # Aregamos un nuevo elemento a nuestro diccionario    
print(my_dict)


del my_dict["Ciudad"]   
print(my_dict)


print("Apellido" in my_dict) # Necesitamos buscar por clave no por valor
print("Peretti" in my_dict)


print(my_dict.items())

print(my_dict.keys())

print(my_dict.values())


my_new_dict = dict.fromkeys(("Nombre", 1, "Ciudad"))     # Creamos un diccionario vacío
print(my_new_dict)