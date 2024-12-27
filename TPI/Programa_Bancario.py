"""""
Programando una APP bancaria básica.
"""""


def mostrar_saldo(saldo):
    print(f"Tu saldo actual es: {saldo:.2f}$")


def depositar():
    monto = float(input("Ingrese la cantidad de dinero: "))
    if monto < 0:
        print("La cantida introducida no es válida.")
        return 0
    else:
        return monto
    
def retiro(saldo):
    monto = float(input("Ingrese la cantidad a retirar: "))
    if monto > saldo:
        print("Fondos insuficientes.")
        return 0
    elif monto < 0:
        print("La cantidad introducida no es válida.")
        return 0
    else:
        return monto
    

def menu_entrada():

    saldo = 0
    en_ejecucion = True


    while en_ejecucion:

        print("Programa Bancario.")
        print("1 - Mostrar Saldo.")
        print("2 - Depositar.")
        print("3 - Retirar.")
        print("4 - Salir.")

        opcion = input("Ingrese una opción (1-4): ")

        if opcion == "1":
            mostrar_saldo(saldo)
        elif opcion == "2":
            saldo += depositar()
        elif opcion == "3":
            saldo -= retiro(saldo)
        elif opcion == "4":
            en_ejecucion = False
            print("Saliendo del programa.")
        else:
            print("Elección no válida.")

if __name__ == '__main__':
    menu_entrada()



