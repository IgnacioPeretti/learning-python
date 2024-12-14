total_unidades = 19 

equipo = ["Argentina", "Mexico", "Arabia Saudita", "Polonia"]

figuritas = [[None] * total_unidades for _ in equipo]

posicion_actual_equipo = [0] * len(equipo)


def añadir_figuritas(indice):

    while True:
                
        if posicion_actual_equipo[indice] == total_unidades:
            print(f"Felicidades completaste el equipo {equipo[indice]}  !")
            break

        figurita = input(f"Ingrese las unidades o (exit) para salir: ")

        if figurita.lower() == "exit":
            print("Volviendo al menu principal.")
            break

        if figurita in figuritas:
            print(f"La figurita {figuritas} ya la tenes.")

        else:
            figuritas[indice] [posicion_actual_equipo[indice]] == figurita
            posicion_actual_equipo[indice] += 1
            print(f"Figurita añadida: {figuritas}")


        porcentaje = (posicion_actual_equipo[indice] / total_unidades) * 100
        print(f"Usted tiene completado un {porcentaje:.2f} % de las figuras de equipo {equipo[indice]}.")


print("Bienvenido al programa del Mundial de la copa 2022.")

while True:



    print("""Tiene 5 opciones para elegir:  
            1 - Añadir figura de Argentina
            2 - Añadir figura de Mexico
            3 - Añadir figura de Arabia Saudita
            4 - Añadir figura de Polonia 
            5 - Consultar el porcentaje del grupo completado
            6 - Salir del programa.         
            """)

    opcion = int(input("Ingrese una opción: "))


    if int(opcion) == 6:
        print("Saliendo del Programa. Gracias.")
        break

    elif int(opcion) in [1, 2, 3, 4]:
        indice = int(opcion) - 1
        añadir_figuritas(indice)

    elif int(opcion) == 5:
        total_figuras = sum(posicion_actual_equipo)
        total_unidades_grupoc = total_unidades * len(equipo)
        porcentaje_grupo_completado = (total_figuras / total_unidades_grupoc) * 100

        print(f"Lleva completado un {porcentaje_grupo_completado:.2f}% del grupo C.")

        if porcentaje_grupo_completado == 100:
            print("¡Felicitaciones! ¡Has completado todo el grupo C!")

    else:
        print("Opción no válida. Intente nuevamente.")