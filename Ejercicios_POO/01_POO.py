"""
Ejercicio de herencia y uso de super.

Crear un sistema para una escuela. En este sistema, vamos a tener dos clases principales:
Persona y Estudiante. La clase Persona tendra los atributos de nombre y edad y un método
que imprima el nombre y la edad de la persona. La clase Estudiante heredará de la clase 
Persona y también tendra un atributo adicional Grado y un método que imprima el grado de 
el estudiante.

Deberás utiliza super en el método de inicialización (init) para reutilizar código de la clase
padre (Persona). Luego crea una instancia de la clase Estudiante e imprime sus atributos y utiliza
sus métodos para asegurarte de que todo funciona correctamente.
"""

class Persona:
    def __init__(self, nombre, edad):
        
        self.nombre = nombre
        self.edad = edad
    
    def Presentarse(self):
        print(f"Hola, mi nombre es {self.nombre} y tengo {self.edad} años.")


class Estudiante(Persona):
    def __init__(self, nombre, edad, grado):
        super().__init__(nombre, edad)

        self.grado = grado

    def mostrar_Grado(self):
        print(f"Estoy en {self.grado} grado.")


ignacio = Estudiante("Ignacio", "24", "3")

ignacio.Presentarse()

ignacio.mostrarGrado()
    