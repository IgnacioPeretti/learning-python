# Operadores #


"""""
los operadores son símbolos que permiten realizar operaciones sobre variables y valores.

Operadores aritméticos: Realizan operaciones matemáticas básicas.

+ (suma)
- (resta)
* (multiplicación)
/ (división)
// (división entera)
% (módulo)
** (exponenciación)

"""""

print(3 + 4)
print(3 - 4)
print(3 * 4)
print(3 / 4)
print(10 % 3)  # nos muestra el resto
print(10 // 3)
print(2 ** 3) 
print(2 ** 3 + 3 - 7 / 1 // 4)


print("Hola " + "Nacho, " + "¿Todo bien?")

print("Hola " + str(5))
print("Hola " * 2)
print("Hola " * (2 ** 3))


my_float = 2.5 * 2

print("Hola " * int(my_float))  # Lo paso a entero (int)



# Solo podemos concatenar cadenas
# print("Hola " + 5) Aquí nos daría este error, TypeError: can only concatenate str (not "int") to str



"""""
Operadores de comparación: Comparan dos valores y devuelven un booleano (True o False).

== (igual)
!= (diferente)
> (mayor que)
< (menor que)
>= (mayor o igual que)
<= (menor o igual que)

"""""

print(3 > 4)
print(3 < 4)
print(3 >= 4)
print(3 <= 4)
print(3 == 4)
print(3 != 4)
print(3 > 4 == 2)
print(3 > 4 > 2)
print(5 > 4 > 3)


# Ordenación alfabética por ASCII

print( " Hola " > " Nacho ")

print( " Hola " == " Hola ")

print( " Hola " >= " Dos ")

print( " Hola " != " Hola1 ")


"""""
Operadores lógicos: Operan sobre valores booleanos.

and (y)
or (o)
not (no)

"""""

print(3 > 4 and "Hola" > "Nacho")

print(3 < 4 and "Hola" < "Nacho")

print(3 < 4 or "Hola" > "Nacho")

print(3 > 4 or "Hola" > "Nacho")

print(3 > 4 and (3 > 2) and (3 > 4))

print(3 < 4 and (3 > 2) or (3 < 4))

print( 3 < 4 or ("Hola" > "Nacho" and 4 == 4 ))

print(not(3 > 2))

print(not(3 > 4))


""""""

""""""