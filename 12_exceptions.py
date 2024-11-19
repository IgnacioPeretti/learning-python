### Exception Handling ###

"""""
Una excepción es un evento o error que interrumpe el flujo normal de un programa.
Por ejemplo, si intentas dividir un número por cero, o si intentas acceder a un archivo que no existe, Python generará una excepción.

Python utiliza un mecanismo de manejo de excepciones que se basa en los bloques try, except, else y finally.
"""""
numberOne = 5
numberTwo = 1
numberTwo = "1"


try:
    print(numberOne + numberTwo)
    print("No se a producido un error")
except:
    print("Se ha producido un error")
else: # Opcional
    # Se ejecuta si no se produce una excepción
    print("La ejecución continúa correctamente")
finally: # Opcional
    # Se ejecuta siempre
    print("La ejecución continúa")


# Excepciones por tipo

try:
    print(numberOne + numberTwo)
    print("No se ha producido un error")
except TypeError as typeError:
    print("Se ha producido un error TypeError")
    print(typeError)
except ValueError as valueError:
    print("Se ha producido un error ValueError")
    print(valueError)
except Exception as genericError:
    print("Se ha producido un error genérico")
    print(genericError)



print("Segundo ejemplo")


try:
    # Código que puede generar una excepción
    x = 1 / 0  # Esto generará un error de división por cero
except ZeroDivisionError:
    # Aquí se maneja la excepción
    print("No se puede dividir por cero")
except Exception as e:
    # Aquí se manejaría cualquier otra excepción
    print(f"Ocurrió un error: {e}")
else:
    # Este bloque se ejecuta si no hay excepciones
    print("Todo salió bien")
finally:
    # Este bloque siempre se ejecuta
    print("Este código se ejecutará siempre")
