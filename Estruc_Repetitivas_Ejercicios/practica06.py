"""""
Escribir un programa que almacene una cadena de caracteres "contraseña" en una variable,
pregunte al usuario por la contraseña hasta que reproduzca la contraseña correcta.  
"""""



contraseña_correcta = "contraseña"

intentos = 3


for i in range(intentos):
    contraseña = input("Ingrese una contraseña: ")

    if contraseña == contraseña_correcta:
        print("La contraseña es correcta.")
        break
    else:
        print("Contraseña incorrecta, intente nuevamente.")

else:
    print("Has agotado el número de intentos.")




print("Ahora con bucle while.")



contraseña_correcta = "contraseña"

intentos = 0

intentos_maximos = 3

while intentos < intentos_maximos:
    contraseña = input("Ingrese una contraseña: ")

    if contraseña == contraseña_correcta:
        print("La contraseña es correcta.")
        break
    else:
        print("Contraseña incorrecta, intente nuevamente.")

    intentos += 1

if intentos == intentos_maximos:
    print("Has agotado todos los intentos.")