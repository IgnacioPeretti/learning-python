

from abc import ABC, abstractmethod

class Vehiculo(ABC):               # La clase abstracta Vehiculo define un comportamiento común.
    @abstractmethod
    def acelerar(self):
        pass

    @abstractmethod
    def frenar(self):
        pass

class Coche(Vehiculo):                        # Las clases Coche y Bicicleta implementan esos comportamientos de manera específica.
    def acelerar(self):
        print("El coche está acelerando.")

    def frenar(self):
        print("El coche está frenando.")

class Bicicleta(Vehiculo):
    def acelerar(self):
        print("La bicicleta está acelerando.")

    def frenar(self):
        print("La bicicleta está frenando.")

                                             
# El uso del polimorfismo permite interactuar con los vehículos sin conocer sus detalles internos.

vehiculos = [Coche(), Bicicleta()]
for v in vehiculos:
    v.acelerar()
    v.frenar()
