"""""
El encapsulamiento nos ayuda a proteger los datos de nuestros atributos y métodos controlando el acceso a ellos.
Mejora la mantención y legibilidad del código, también fomenta la modularidad del mismo.
"""""


class Miclase:
    def __init__(self):
        self.__atributo_privado = "Valor"    # Guion bajo es protegido y doble guion bajo es privado.

    def __hablar(self):
        print("Hola, como estas?")


objecto = Miclase()

print(objecto.__hablar)
