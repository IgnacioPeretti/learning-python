"""""
Los getters y setters son métodos en la Programación Orientada a Objetos (POO) 
que se utilizan para obtener (get) y modificar (set) el valor de los atributos 
privados o protegidos de una clase.

Estos métodos son una práctica común para implementar el encapsulamiento.

¿Por qué usar getters y setters?

Control del acceso, Encapsulamiento, Mantenimiento, Legibilidad y seguridad.
"""""
class Persona:
    def __init__(self, nombre, edad):
        self.__nombre = nombre
        self.__edad = edad

    def get_nombre(self):
        return self.__nombre
    
    def set_nombre(self, nuevo_nombre):
        self.__nombre = nuevo_nombre
    

nacho = Persona("Nacho", "24")

nombre = nacho.get_nombre()
print(nombre)


nacho.set_nombre("Ignacio")

nombre = nacho.get_nombre()

print(nombre)