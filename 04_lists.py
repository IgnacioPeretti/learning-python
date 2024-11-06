# Listas 
# Estructura de datos


my_list = list()
my_other_list = []


print(len(my_list))


my_list = [35, 23, 16, 19, 20, 20]

print( my_list )


print(len(my_list))


my_other_list = [24, 1.77, "Ignacio", "Peretti"]

print(my_other_list)

print(type(my_other_list))

print(my_other_list[0])
print(my_other_list[1])
print(my_other_list[2])
print(my_other_list[3])

print(my_other_list[-1])
print(my_other_list[-2])
print(my_other_list[-3])
print(my_other_list[-4])

# print(my_other_list[-5]) INDEX ERROR


print(my_other_list.count("Ignacio"))  
# Cuenta el numero de ocurrencias de un elemento dentro de la lista
print(my_list.count(20))

age, height, name, surname = my_other_list

print(age)


print(my_list + my_other_list)

my_other_list.append("Córdoba") # Agrega un elemento a la lista
print(my_other_list)


my_other_list.insert("Argentina")
print(my_other_list)


my_other_list.remove("Argentina")
print(my_other_list)


my_list.remove(20) # Remueve de la lista un elemento
print(my_list)


my_list.pop() # Por defecto este eliminará el último elemento
print(my_list)

my_list.pop(2) 
print(my_list)

my_pop_element = my_list.pop(2)
print(my_pop_element)   # Nos retorna el elemento que sera eliminado
print(my_list)