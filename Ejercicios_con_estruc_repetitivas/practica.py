"""""
Lea N y halle el resultado de la sumatoria 1/1+1/2+1/3+1/4+1/n
"""""

n = int(input("Ingrese el valor de N: "))

sumatoria = 0

for i in range(1, n + 1):
    sumatoria += 1/i


print("El resultado de la sumatoria es:", sumatoria)



palabra = input("Ingrese una palabra: ")

for i in range(1, 10):
    print(palabra)