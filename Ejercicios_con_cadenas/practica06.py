"""""
Escribir un programa que pregunte por consola el precio de un producto en euros con dos decimales y
muestre por pantalla el número de euros y el número de céntimos del precio introducido.

"""""


producto = input("Ingrese el precio del producto en euros: ")

num_euros = producto.split(".")[0]

num_centimos = producto.split(".")[1]

print(f"El total es: {num_euros} euros con {num_centimos} centimos")