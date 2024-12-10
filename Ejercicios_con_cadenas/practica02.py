"""""
Los teléfonos de una empresa tienen el siguiente formato prefijo-número-extension donde el prefijo es el
código del país +34, y la extensión tiene dos dígitos (por ejemplo +34-913724710-56). Escribir un programa
que pregunte por un número de teléfono con este formato y muestre por pantalla el número de teléfono sin el
prefijo y la extensión.

"""""


while True:
    numero = input("Ingrese su número de teléfono en el formato +34-XXXXXXXXX-56 (o escriba 'Exit' para salir): ")

    if numero.lower() == "exit": 
        print("Saliendo del programa.")
        break

    
    prefijo = "+34-"
    extension = "-56"
    numero_sin_prefijo_y_extension = numero[4:-3]             # Podemos usar [len(prefijo):-len(extension)]


    print(f"El número sin prefijo ni extensión es: {numero_sin_prefijo_y_extension}")
