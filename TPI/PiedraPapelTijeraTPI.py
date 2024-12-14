import random

opciones = ["piedra", "papel", "tijera"]
sep = "_" * 15
juego= 0
print("..:::BIENVENIDO:::..")
juego= int(input("1. Presione 0 para iniciar el juego.\n2. Presione 1 si quiere volver al menu.\n"))

print("¡Comienza el juego!")
while juego==0:
    user = input("¡Tu Elijes! piedra, papel o tijera: ").lower()
    if user not in opciones:
        print("\n Movimiento no valido")
        continue
    pc = random.choice(opciones)
    print(f"\nLa PC a seleccionado {pc}")
    if user == pc:
        print(f"\nEmpate!, ambos eligieron {user}")

    elif user == "piedra" and pc == "tijera":
        print(f"\nGanaste!,{user} gana en contra de {pc}")
    elif user == "tijera" and pc == "papel":
        print(f"\nGanaste!,{user} gana en contra de {pc}")
    elif user == "papel" and pc == "piedra":
        print(f"\nGanaste!,{user} gana en contra de {pc}")
    else:
        print(f"\nPerdiste, {user} pierde contra {pc}")
    print()
    print(f"{sep}Fin del juego{sep}")
    juego = int(input("¿Quieres seguir jugando?\n1. Presione 0 para iniciar el juego.\n2. Presione 1 si quiere volver al menu.\n"))




