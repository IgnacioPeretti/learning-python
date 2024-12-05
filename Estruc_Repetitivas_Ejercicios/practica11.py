"""""
Realice un programa que determine si un numero de 3 dígitos
ingresado por el usuario es no capicúa
"""""

while True:
    
    n = int(input("Ingrese un número de 3 dígitos (o 0 para salir): "))
    
    if n == 0:
        print("Programa terminado.")
        break

    if n < 100 or n > 999:
        print("El número ingresado no tiene 3 dígitos. Intente de nuevo.")
        continue

    
    n_str = str(n)
    if n_str == n_str[::-1]:
        print(f"El número {n} es capicúa.")
    else:
        print(f"El número {n} no es capicúa.")
    


