"""""
Escribir un programa que pida al usuario que introduzca una frase en la consola y muestre por pantalla la
frase invertida.

"""""

while True:

    frase = input("Intodruzca una frase: ")
   


    if frase.lower() == "exit":
        print("Saliendo del programa.")
        break

    frase_invertida = frase[::-1]    
    print(f"La frase invertida es {frase_invertida}")

