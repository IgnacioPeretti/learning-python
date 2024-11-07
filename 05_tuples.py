### Tuples ###



my_tuple = tuple()
my_other_tuple = ()


my_tuple = (35, 1.77, "Ignacio", "Ignacio", "Peretti")
print(my_tuple)
print(type(my_tuple))


print(my_tuple[0])
print(my_tuple[-1])

print(my_tuple.count("Ignacio"))

print(my_tuple.index("Peretti"))  # Muestra el indice del elemento

"""""
my_tuple[1] = 1.80
print(my_tuple)  

TypeError: 'tuple' object does not support item assignment

Las tuplas son inmutables, podemos guardar datos pero no podemos asignarle luego.
"""""

my_other_tuple = (20, 21, 22, 23)

my_sum_tuple = my_tuple + my_other_tuple

print(my_sum_tuple)

print(my_sum_tuple[3:6])



my_tuple = list(my_tuple)
print(type(my_tuple))

my_tuple[4] = "Nacho"
my_tuple.insert(1, "Villa María")

my_tuple = tuple(my_tuple)
print(my_tuple)
print(type(my_tuple))


del my_tuple