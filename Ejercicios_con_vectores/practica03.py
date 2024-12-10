"""""
Cargar un vector con las alturas de los N alumnos de un curso. Determinar la media y luego informar
cuántos alumnos son más altos que la media y cuántos más bajos
"""""


vector = []
altura_total = 0


for i in range(0, 5):
    altura = int(input(f"Ingrese la altura del alumno {i+1}: "))
    vector.append(altura)


for i in vector:
    altura_total += i

promedio = altura_total / len(vector)

print(f"La altura promedio del vector es: {promedio}")


mas_altos = 0
mas_bajos = 0
altura_media = 0

for i in vector:
    if i > promedio:
        mas_altos += 1
    elif i < promedio:
        mas_bajos += 1
    else:
        altura_media += 1

print(f"Alumnos con altura promedio {altura_media}")    
print(f"Alumnos mas altos que la media {mas_altos}")
print(f"Alumnos mas bajos que la media {mas_bajos}")


    