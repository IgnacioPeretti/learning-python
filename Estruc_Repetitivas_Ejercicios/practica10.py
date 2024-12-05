"""""
Crear un programa que permita al usuario ingresar los montos
de las compras de un cliente (se desconoce la cantidad de datos
que ingresará, la cual puede cambiar en cada ejecución), cortando
el ingreso de datos cuando el usuario ingrese el monto 0.

Si ingresa un monto negativo, no se debe procesar y debe pedir que
ingrese un monto nuevo, al finalizar le informará el total a pagar
teniendo en cuenta que, si las ventas superan el total de $1000 se
le aplicará un 10% de descuento 
"""""

total_ventas = 0

while True:
    n = int(input("Ingrese el monto de sus compras (ingrese 0 para salir): "))
    if n == 0:
        break
    elif n < 0:
        print("Error: No puede ingresar un monto negativo. Ingrese nuevamente.")

    print(f"El valor de su compra es de: {n}")
    total_ventas += n


if total_ventas >= 1000:
    descuento = (total_ventas * 10) / 100
    total_con_descuento = total_ventas - descuento
    print("Tiene un descuento del 10%")
    print(f"El valor total de la compra con el descuento es de: {total_con_descuento}")
else:
    print("No se aplico ningún descuento.")
    print(f"El valor total de su compra es: {total_ventas}") 

