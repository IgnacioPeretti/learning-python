"""""
Dado un numero entero N de 12 cifras ingresado por el usuario,
elimine de el todos los digitos mayores a 5.
Ej: N = 156821568290  = 1521520
"""""


while True:
    num = input("Ingrese un número de 12 cifras (o escriba 'salir' para terminar): ")

    if num.lower() == "salir":
        print("Saliendo del programa.")
        break

    if len(num) != 12:
        print("El número no tiene 12 cifras, intente nuevamente.")
        continue

    num_retorno = ""

    for digito in num:
        if int(digito) <= 5:  
            num_retorno += digito  

    print("El número resultante es:", num_retorno)

    
