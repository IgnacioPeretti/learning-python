import random
import time



def tragamonedas():
    opciones = ["🍌","🍋","🍎","🍉"]
    resultado = []

    for x in range(3):
        rueda = random.choice(opciones)
        resultado.append(rueda)
        print(f"{rueda}", end =  " ", flush = True)
        time.sleep(1.5)

    if resultado[0] == resultado[1] == resultado[2]:
        print("\nJACKPOT!")


while True:

    print("\nBienvenido al tragamonedas.")
    salir = int(input("Ingresa 0 si quieres salir del juego o 1 si quieres jugar."))

    if salir == int(1):
        tragamonedas()

    else: 
        salir == int(0)
        print("Saliendo del programa.")
        break 
