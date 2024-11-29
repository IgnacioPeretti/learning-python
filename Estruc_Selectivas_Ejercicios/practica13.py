"""""
La pizzería Bella Napoli ofrece pizzas vegetarianas y no vegetarianas a sus clientes. Los
ingredientes para cada tipo de pizza aparecen a continuación.

Ingredientes vegetarianos: Pimiento y tofu.
Ingredientes no vegetarianos: Peperoni, Jamón y Salmón.

Escribir un programa que pregunte al usuario si quiere una pizza vegetariana o no, y en
función de su respuesta le muestre un menú con los ingredientes disponibles para que elija.
Solo se puede eligir un ingrediente además de la mozzarella y el tomate que están en todas
la pizzas. Al final se debe mostrar por pantalla si la pizza elegida es vegetariana o no y
todos los ingredientes que lleva.

"""""


print("..::BIENVENIDO A PIZZERIA BELLA NAPOLI::..")


# Ingredientes comunes
ing_tomate = "tomate"
ing_muzz = "muzzarella"

# Ingredientes para pizza vegetariana
ing_ceb = "cebolla"
ing_dob_queso = "doble queso"
ing_rucula = "rucula"

# Ingredientes para pizza no vegetariana
ing_jamon = "jamon"
ing_huevo = "huevo"
ing_peperoni = "peperoni"
ing_salmon = "salmón"


seleccion_pizza = input("¿Quiere pedir una pizza vegetariana? (si/no): ").lower()

if seleccion_pizza == "si":
    print("A continuación le mostramos los ingredientes disponibles para pizza vegetariana:")
    print(ing_ceb, ing_rucula, ing_dob_queso)

    ingrediente = input("Puede elegir agregar 1 ingrediente (cebolla, rucula, doble queso): ").lower()
    if ingrediente in [ing_ceb, ing_rucula, ing_dob_queso]:
        print(f"Los ingredientes de su pizza vegetariana serán {ing_tomate}, {ing_muzz} y {ingrediente}.")
    else:
        print("Error: Ingrediente no válido. Intente nuevamente.")
    
elif seleccion_pizza == "no":
    print("A continuación le mostramos los ingredientes disponibles para pizza no vegetariana:")
    print(ing_ceb, ing_rucula, ing_dob_queso, ing_jamon, ing_huevo, ing_peperoni, ing_salmon)

    ingrediente = input("Puede elegir agregar 1 ingrediente (cebolla, rucula, doble queso, jamon, huevo, peperoni, salmon): ").lower()
    if ingrediente in [ing_ceb, ing_rucula, ing_dob_queso, ing_jamon, ing_huevo, ing_peperoni, ing_salmon]:
        print(f"Los ingredientes de su pizza no vegetariana serán {ing_tomate}, {ing_muzz} y {ingrediente}.")
    else:
        print("Error: Ingrediente no válido. Intente nuevamente.")

else:
    print("Error, opción no válida. Intente nuevamente.")



   

        


    


