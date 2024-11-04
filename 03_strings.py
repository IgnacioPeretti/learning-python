my_String = " My String "
my_other_string = " My other String "

print(len(my_other_string))

print(len(my_String))

print(my_String + " " + my_other_string)

my_new_line_string = "String con salto\nde línea"

print(my_new_line_string)


print(my_String +""+ my_other_string + my_new_line_string)

my_tab_string = "\tString con tabulación"
print(my_tab_string)

my_scape_string = "\\t String \\n escapado"
print(my_scape_string)



# Formatear Strings



name, surname, age, temperatura = "Ignacio", "Peretti", 24, 27.5



"""""

%s: se utiliza para formatear cadenas de texto (strings). Se usa para insertar texto en una cadena.

%d: se utiliza para formatear números enteros (integers). Se usa cuando quieres insertar un número entero en una cadena.

%f: Este se utiliza para formatear números de punto flotante (floats). Es útil para insertar números decimales en una cadena.

"""""

print("Mi nombre es {} {} y mi edad es {}, la temperatura de hoy es de {} grados".format(name, surname, age, temperatura))

print("Mi nombre es %s %s y mi edad es %d, la temperatura de hoy es de %f grados" %(name, surname, age, temperatura))

print(f"Mi nombres es {name} {surname} y mi edad es {age}, la temperatura de hoy es de {temperatura} grados.") 

# Desempaquetado de caracteres

language = "Python"

a, b, c, d, e, f = language 

print(a)
print(b)
print(c)
print(d)
print(e)
print(f)



# División

language_slice = language[1:3]
print(language_slice)


language_slice = language[1:]
print(language_slice)

language_slice = language[-2]
print(language_slice)


# Reverse

reversed_language = language[::-1]
print(reversed_language)


# Funciones

print(language.capitalize())
print(language.upper())
print(language.count("t"))
print(language.isnumeric())
print("1".isnumeric())
print(language.lower())
print(language.upper().isupper())
print(language.startswith("Py"))

