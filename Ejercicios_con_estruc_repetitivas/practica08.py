"""""
Una fábrica produce botellas de vidrio reciclando botellas usadas. Suponiendo botellas similares,
la maquina con X botellas usadas puede fabricar 1 botella nueva.

Realice un algoritmo para encontrar la cantidad total acumulada de botellas que pueden fabricarse
a partir de N botellas en el mercado, reciclandolas repetidamente hasta que ya no queden suficientes 
botellas para reciclar.


Por ejemplo, Si n = 70, x = 4, la respuesta entregada por el algoritmo es 23 siguiendo el siguiente 
proceso:

Primer reciclaje : Se fabrican 70/4 = 17 botellas y sobran 2
Segundo reciclaje: Se fabrican n = 17 + 2 = 19 botellas y sobran 3
Tercer reciclaje:  n = 4 + 3 = 7, se fabrican 7/4 = 1 sobran 3
Cuarto reciclaje: n = 1 + 3 = 4, se fabrican 4/4 = 1 botellas y ya no quedan botellas para reciclar

El algoritmo termina y muestra el acumulado
Total acumulado: 17 + 4 + 1 + 1 = 23

"""""


def calcular_botellas_acumuladas(n, x):
    total_acumulado = 0
    sobrantes = 0


    while n > 0:

        fabricadas = n // x
        sobrantes = n % x


        total_acumulado += fabricadas

        n = fabricadas + sobrantes

        if n < x:
            print("No hay suficientes botellas a reciclar.")
            break
    
    return total_acumulado


n = int(input("Ingrese la cantidad de botellas a reciclar: "))
x = 4

resultado = calcular_botellas_acumuladas(n, x)

print(f"El total acumulado de botellas fabricadas es: {resultado}")

