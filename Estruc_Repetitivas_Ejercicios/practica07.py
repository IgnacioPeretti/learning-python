"""""
Escribir un programa que muestre el eco de todo lo que el usuario introduzca
hasta que introduzca la palabra "salir" que terminará
"""""


salida = "salir"



while True:

    entrada = input("Introduzca una palabra o (salir) para terminar: ")

    if entrada == salida:
        print("Programa terminado.")
        break
    
    print("Eco:", entrada * 3)