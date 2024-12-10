"""""
Se tienen los costos de producción de tres departamentos (dulces, bebidas y conservas), correspondientes
a los 12 meses del año
Elaborar un programa que pueda proporcionar la siguiente información:
a) ¿En qué mes (número) se registró el mayor costo de producción de dulces?
b) Promedio anual de los costos de producción de bebidas.
c) ¿En qué mes se registró el menor costo de producción de bebidas?
d) ¿Cuál fue el departamento que tuvo el menor costo de producción en Agosto?

"""""
dulces = []
bebidas = []
conservas = []

print("Ingrese los costos de producción para los 12 meses del año:")

for mes in range(12):
    print(f"Mes {mes + 1}:")
    dulces.append(float(input("  Dulces: ")))
    bebidas.append(float(input("  Bebidas: ")))
    conservas.append(float(input("  Conservas: ")))

# ¿En qué mes (número) se registró el mayor costo de producción de dulces?

mayor_costo_dulces = max(dulces)  
mes_mayor_dulces = dulces.index(mayor_costo_dulces) + 1  

print(f"a) El mayor costo de producción de dulces fue en el mes {mes_mayor_dulces}.")


# Promedio anual de los costos de producción de bebidas.

suma_bebidas = sum(bebidas)  
promedio_bebidas = suma_bebidas / 12  

print(f"b) El promedio anual de los costos de producción de bebidas es: {promedio_bebidas:.2f}")


# ¿En qué mes se registró el menor costo de producción de bebidas?

menor_costo_bebidas = min(bebidas)
mes_menor_bebidas = bebidas.index(menor_costo_bebidas) + 1 

print(f"c) El menor costo de producción de bebidas fue en el mes {mes_menor_bebidas}.")



# ¿Cuál fue el departamento que tuvo el menor costo de producción en Agosto?

agosto = 7  
costo_agosto_dulces = dulces[agosto]
costo_agosto_bebidas = bebidas[agosto]
costo_agosto_conservas = conservas[agosto]


if costo_agosto_dulces < costo_agosto_bebidas and costo_agosto_dulces < costo_agosto_conservas:
    menor_departamento = "dulces"
elif costo_agosto_bebidas < costo_agosto_conservas:
    menor_departamento = "bebidas"
else:
    menor_departamento = "conservas"

print(f"d) En agosto, el departamento con menor costo de producción fue: {menor_departamento}.")