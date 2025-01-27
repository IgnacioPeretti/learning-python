"""""
SRP - Single Responsibility Principe - Principio de Responsabilidad Única

Una clase debe tener una única razón para cambiar, lo que significa que debe tener una única responsabilidad.

Ejemplo: Imagina que tienes una clase Auto que maneja tanto las operaciones del vehículo (como arrancar el motor, conducir, etc.)
como el manejo del tanque de combustible (llenar el tanque, controlar el nivel de combustible, etc.).
Esto viola el principio de Responsabilidad Única.

Para aplicar SRP, dividimos las responsabilidades en diferentes clases:

La clase Auto manejará solo las operaciones relacionadas con el vehículo.
Crearemos una clase separada Tanque_Combustible que se encargue del manejo del combustible.

Así mantenemos cada clase enfocada en una única tarea.
"""""

class Auto:
    def __init__(self, tanque):
        self.posicion = 0
        self.tanque = tanque

    def mover(self, distancia):
        if self.tanque.obtener_combustible() >= distancia / 2:
            self.posicion += distancia
            self.tanque.usar_combustible(distancia / 2)
            print("Has movido el auto exitosamente.")
        else:
            print("No hay suficientes combustible.")

    def obtener_posicion(self):
        return self.posicion

class Tanque_Combustible:
    def __init__(self):
        self.combustible = 100

    def agregar_combustible(self, cantidad):
        self.combustible += cantidad
    
    def obtener_combustible(self):
        return self.combustible
    
    def usar_combustible(self, cantidad):
        self.combustible -= cantidad

tanque = Tanque_Combustible()

auto = Auto(tanque)


print(auto.obtener_posicion())
auto.mover(10)
print(auto.obtener_posicion())
auto.mover(20)
print(auto.obtener_posicion())
auto.mover(60)
print(auto.obtener_posicion())
auto.mover(100)
print(auto.obtener_posicion())
auto.mover(10)
print(auto.obtener_posicion())
auto.mover(10)                            # Ya no podemos mover el auto, nos quedamos sin combustible.
print(auto.obtener_posicion())
