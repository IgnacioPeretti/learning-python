"""""
Realizar un algoritmo para determinar cuánto ahorrará una persona en un año,
si al final de cada mes deposita cantidades variables de dinero;
además, se quiere saber cuánto lleva ahorrado cada mes.
"""""

ahorro = 0

print("Calculadora de ahorro anual")
print("-" * 30)


for i in range(1, 13):
    while True:
            
            sueldo = float(input(f"Ingrese lo que quiere ahorrar este mes (mes {i}): "))

            if int(sueldo) == 0:
                 print("Este mes no se ahorró dinero.")
            
            if sueldo < 0:
                print("Por favor, ingrese una cantidad positiva.")
                continue
            break

    ahorro += sueldo
    print(f"Mes {i}: lleva ahorrado ${ahorro:.2f}")


print("-" * 30)
print(f"La cantidad total ahorrada en el año es: ${ahorro:.2f}")
