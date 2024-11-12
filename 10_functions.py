### Funciones ###


def my_function ():
    print("Esto es una función")



my_function()
my_function()
my_function()

def suma_two_values (first_number, second_number): # Estos valores podemos llamarlos argumentos o parametros
    print(first_number + second_number)  # Aqui tendremos parametros de salida

suma_two_values(5,5)
suma_two_values(5231,5213)
suma_two_values("5","7")  # concatena   



def suma_two_values_with_return (first_value, second_value):
    return first_value + second_value    # nos retorna el valor de la suma de ambos elementos


resultado = suma_two_values_with_return(10, 5)
print(resultado)



def print_name(name, surname):
    print(f"{name} {surname}")   

print_name(name= "Ignacio", surname= "Peretti")


def print_name_with_default (name, surname, alias = "Sin alias"):        # Podemos asignarle un valor por defecto
        print(f"{name} {surname} {alias}")   

print_name_with_default(name= "Ignacio", surname= "Peretti", alias= "Nacho")


def print_texts(*texts):   # El asterisco nos permite pasarle la cantidad de argumentos que queramos
    for text in texts:
        print(text.upper())

print_texts("Hola nacho")

print_texts("Hola nacho", "Como estas?", "Lindo día")