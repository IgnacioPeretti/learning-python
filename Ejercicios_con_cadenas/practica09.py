"""""
Escribir un programa que pregunte el nombre el un producto, su precio y un número de unidades y muestre
por pantalla una cadena con el nombre del producto seguido de su precio unitario con 6 dígitos enteros y 2
decimales, el número de unidades con tres dígitos y el coste total con 8 dígitos enteros y 2 decimales.
"""""

producto = input("Ingrese nombre, precio y unidades del producto: ")

nombre, precio, unidades = producto.split(",")

precio = float(precio)
unidades = int(unidades)

total_compra = precio * unidades

print(f"Nombre del producto:{nombre}, Precio unitario: {precio:06.2f}, Número de unidades:{unidades:03d}. El total es:{total_compra:08.2f}")