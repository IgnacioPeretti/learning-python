# Operadores


# Operadores ariméticos

print(f"La suma de 10 + 3 es = {10 + 3} ")

print(f"La resta de 10 - 3 es = {10 - 3} " )

print(f"La multiplicación de 10 * 3 es = {10 * 3} ")

print(f"La división de 10 entre 3 es = {10 / 3} ")

print(f"El modulo de 10 % 3 es = {10 % 3} ")

print(f"El exponente de 10 a la 3 es = {10 ** 3} " )

print(f"La división entera de 10 entre 3 es = {10 // 3} " )


# Operadores de comparación

print(f"Igualdad: 10 == 3 es {10 == 3} ")

print(f"Desigualdad: 10 != 3 es {10 != 3} ")

print(f"Mayor que: 10 > 3 es {10 > 3} ")

print(f"Menor que: 10 < 3 es {10 < 3} ")

print(f"Mayor o igual que: 10 >= 3 es {10 >= 10} ")

print(f"Menor o igual que: 10 <= 3 es {10 <= 3}")


# Operadores lógicos

# los operadores lógicos son aquellos que operan sobre valores booleanos (verdadero o falso) 

print(f"AND - &&: 10 + 3 == 13 and 5 - 1 == 4 es {10 + 3 == 13 and 5 - 1 == 4} ")

print(f"OR : 10 + 3 == 13 or 5 - 3 == 4 es {10 + 3 == 13 and 5 - 1 == 4} ")  # OR pide que sea verdadera por lo menos 1 de las condiciones

print(f"NOT !: not 10 + 3 == 14 es {10 + 3 == 14}")


# Operadores de asignación 


my_number = 11
print(my_number)

my_number += 1
print(my_number)

my_number -= 1
print(my_number)

my_number *= 2
print(my_number)

my_number /= 2
print(my_number)

my_number %= 2
print(my_number)

my_number **= 1
print(my_number)

my_number //= 1
print(my_number)



# Operadores de identidad

my_new_number = my_number

print(f" my_number is my_new_number es {my_number is my_new_number} ")
print(f" my_number is not my_new_number es {my_number is not my_new_number} ")