### Estructura de datos ###
### Sets ### 

"""""
Un set (o conjunto) en Python es una colección de elementos únicos, no ordenados y mutables.
Es una estructura de datos que permite almacenar varios elementos sin duplicados.

"""""
my_set = set()
my_other_set = {}   # Tenemos dos tipos de estructuras que se definen de este modo, sets y diccionarios


print(type(my_set))
print(type(my_other_set))


my_other_set = {"Ignacio", "Peretti", 24}   # En este momento pasa a ser un set
print(type(my_other_set))


print(len(my_other_set))

my_set.add(5)
print(my_set)  # Output: {1, 2, 3, 4, 5}

my_other_set.add("Córdoba")

print(my_other_set) # Un set no es una estructura ordenada


my_other_set.add("Córdoba")

print(my_other_set) # Un set no admite elementos repetidos 


print("Ignacio" in my_other_set)
print("Ignacios" in my_other_set)



my_other_set.remove("Córdoba")
print(my_other_set)

my_other_set.clear()
print(len(my_other_set))

del my_other_set
# print(my_other_set)   error: no podemos imprimir un delete


my_set = {"ignacio", "peretti", 24}
my_list = list(my_set)

print(my_list)
print(my_list[0])

my_other_set = {"Swift", "Python", "Js"}

my_new_set = my_set.union(my_other_set)

print(my_new_set.union(my_new_set))   # Podemos unirlo y no va a repetir los elementos

print(my_new_set.union(my_new_set).union({"Córdoba", "Argentina"}))

print(my_new_set.difference(my_set))


my_set.add(5)
print(my_set)  # Output: {1, 2, 3, 4, 5}
