"""""
Realizamos una calculadora simple.

"""""

def calcular(operador, num1, num2):
    if operador == "+":
        return num1 + num2
    elif operador == "-":
        return num1 - num2
    elif operador == "*":
        return num1 * num2
    elif operador == "/":
        if num2 == 0:
            raise ValueError("Error: No se puede dividir por cero.")
        return num1 / num2
    else:
        raise ValueError(f"{operador} no es un operador valido.")
    
def main():
    print("CALCULADORA EN PYHTON.")

    try:
        operador = input("Introduce un operador (+ - * /): ").strip()
        operador_validos = ["+", "-", "*", "/"]
        if operador not in operador_validos:
            print(f"El operador {operador} no es válido.")
            return
        
        num1 = float(input("Introduce el primer número:"))
        num2 = float(input("Introduce el segundo número:"))

        resultado = calcular(operador, num1, num2)

        print(f"El resultado es: {round(resultado, 3)}")
    except ValueError as e:
        print(f"Error: {e}")

    print("Gracias por usar el programa!")

if __name__  == '__main__':
    main()