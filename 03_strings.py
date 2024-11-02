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