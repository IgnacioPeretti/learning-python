"""""
Una empresa de producción láctea lleva un control de registro mensual de cantidad de
producción y costo de producción de cada año. Por ejemplo:
Enero: 10 unidades a un costo de $10 cada unidad
Febrero: 8 unidades a un costo de $12 cada unidad
Marzo: 9 unidades a un costo de $11 cada unidad
Abril: 10 unidades a un costo de $12 cada unidad
Mayo: 10 unidades a un costo de $10 cada unidad
Junio: 20 unidades a un costo de $9 cada unidad
Julio: 5 unidades a un costo de $14 cada unidad
Agosto: 9 unidades a un costo de $10 cada unidad
Septiembre: 8 unidades a un costo de $11 cada unidad
Octubre: 7 unidades a un costo de $12 cada unidad
Noviembre: 5 unidades a un costo de $15 cada unidad
Diciembre: 10 unidades a un costo de $11 cada unidad
Dicha empresa necesita saber el promedio de unidades producidas en el año, el promedio
del costo anual del total de la producción Y el nombre del mes cuyo costo de producción
anual fue el más bajo.

"""""

meses = ["Enero", "Febrero", "Marzo", "Abril", "Mayo", "Junio", "Julio", "Agosto", "Septiembre", "Octubre", "Noviembre", "Diciembre"]

unidades_por_mes = [0] * 12
costo_por_mes = [0] * 12
costo_total_por_mes = [0] * 12

for i in range (12):
    unidades = int(input(f"Ingrese las unidades de {meses[i]}: "))
    unidades_por_mes[i] += unidades

print(f"Estos meses las unidades producidas fueron: {unidades_por_mes} ")


for i in range(12):
    costo = int(input(f"Ingrese el costo del mes {meses[i]}: "))
    costo_por_mes[i] = costo

print(f"Estos meses los costos fueron: {costo_por_mes} ")


# Cálculo del total de unidades producidas en el año

total_unidades = 0

for unidades in unidades_por_mes:
    total_unidades += unidades


promedio_prod_anual = total_unidades // 12

print(f"El promedio anual de unidades producidas es de {promedio_prod_anual}")

# Cálculo del costo total de producción por mes

for i in range(12):
    costo_total_por_mes[i] = unidades_por_mes[i] * costo_por_mes[i]

print(f"Costos totales por mes: {costo_total_por_mes}")

costo_total_anual = 0

for costo in costo_total_por_mes:
    costo_total_anual += costo

promedio_costo_anual = costo_total_anual // total_unidades
print(f"El promedio del costo anual del total de la producción es: {promedio_costo_anual}")

# El nombre del mes cuyo costo de producción anual fue el más bajo.

produccion_mas_baja = costo_por_mes[0]
indice_mas_bajo = 0

for i in range(1, 12):
    
    if costo_por_mes[i] < produccion_mas_baja:
        produccion_mas_baja = costo_por_mes[i]
        indice_mas_bajo = i  


print(f"El mes que tuvo el costo de producción mas bajo es: {meses[indice_mas_bajo]} - ${produccion_mas_baja} ")