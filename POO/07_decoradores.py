"""""
¿Qué es un decorador en Python?

Un decorador es una función que recibe como entrada otra función o clase, 
realiza alguna operación (como agregar lógica adicional o modificar comportamiento),
 y devuelve una nueva función o clase.

"""""


class Persona:
    def __init__(self,nombre, edad):
        self.__nombre = nombre
        self.edad = edad

    @property
    def nombre(self):
        return self.__nombre
    
    @nombre.setter  
    def nombre(self, nuevo_nombre):
        self.__nombre = nuevo_nombre

nacho = Persona("Ignacio", "24")

nombre = nacho.nombre
print(nombre)

nacho.nombre = "Nacho"
nombre = nacho.nombre
print(nombre)

