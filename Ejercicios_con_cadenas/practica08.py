"""""
Escribir un programa que pregunte por consola por los productos de una cesta de la compra, separados por
comas, y muestre por pantalla cada uno de los productos en una línea distinta.

"""""


while True:
    productos = input("Ingrese los productos de su compra separados por coma o (ingrese exit para salir): ")

    if productos.lower() == "exit":
        print("Saliendo del programa")
        break

    lista_de_productos = productos.split(",")
    
    print("Los productos de su compra son: ")
    for producto in lista_de_productos:
        print(producto.strip())








