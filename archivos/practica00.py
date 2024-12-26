

# Creamos un archivo


with open("archivo_ejemplo.txt", "w") as archivo:
    archivo.write("Hola, este es mi primer archivo.\n")
    archivo.write("¡Estoy aprendiendo a manejar archivos!")

print("Archivo creado y escrito con éxito.")


# Leemos un archivo 

try:
    with open("archivo_ejemplo.txt", "r") as archivo:
        contenido = archivo.read()
        print(contenido)
except FileNotFoundError:
    print("El archivo no existe.")


# Leer un archivo línea por línea

with open("archivo_ejemplo.txt", "r") as archivo:
    for linea in archivo:
        print(linea.strip())  


# Abrir un archivo en modo agregar

with open("archivo_ejemplo.txt", "a") as archivo:
    archivo.write("\nEste es un nuevo texto añadido al archivo.")

print("Texto añadido con éxito.")



