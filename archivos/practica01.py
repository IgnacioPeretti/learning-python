import os

# Nombre del archivo a borrar

archivo = "archivo_ejemplo.txt"




# Verificar si el archivo existe antes de borrarlo

if os.path.exists(archivo):
    os.remove(archivo)
    print(f"{archivo} ha sido borrado.")
else:
    print(f"El archivo {archivo} no existe.")
