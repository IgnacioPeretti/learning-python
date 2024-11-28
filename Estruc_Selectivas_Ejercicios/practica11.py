"""""
Los tramos impositivos para la declaración de la renta en un determinado país son los
siguientes:

Renta                              Tipo Impositivo

        Menos de 10000          -   5%     
        Entre 10000€ y 20000€   -  15%
        Entre 20000€ y 35000€   -  20%
        Entre 35000€ y 60000€   -  30%
        Más de 60000€           -  45%


Escribir un programa que pregunte al usuario su renta anual y muestre por pantalla el tipo
impositivo que le corresponde.

"""""


renta = int(input("Ingrese su renta anual: "))

if renta < 10000:
    print("Tipo Impositivo: 5%")
    tipo_impositivo = 5
elif renta >= 10000 and renta <= 20000:
    print("Tipo Impositivo: 15%")
    tipo_impositivo = 15
elif renta >= 20000 and renta <= 35000:
    print("Tipo Impositivo: 20%")
    tipo_impositivo = 20
elif renta >= 35000 and renta <= 60000:
    print("Tipo Impositivo: 30%")
    tipo_impositivo = 30
elif renta > 60000:
    print("Tipo Impositivo: 45%")
    tipo_impositivo = 45

calcular_pago = int(round((renta * tipo_impositivo) / 100))


print(f"Usted debe pagar: {calcular_pago} dólares. ")