"""""
Algoritmo que pida caracteres e imprima ‘VOCAL’ si son vocales y ‘NO VOCAL’ en caso contrario,
el programa termina cuando se introduce un espacio.
"""""

vocales = ["a", "e", "i", "o", "u"]

while True:
    caracter = input("Ingrese una letra del abecedario o (exit) para salir: ")

    if caracter.lower() == "exit":
        print("Saliendo del programa.")
        break

    if caracter not in vocales:
        print("NO VOCAL.")
    else:
        print("VOCAL.")
