

from abc import ABC, abstractmethod

class Vehiculo(ABC):
    @abstractmethod
    def acelerar(self):
        pass

    @abstractmethod
    def frenar(self):
        pass

class Coche(Vehiculo):
    def acelerar(self):
        print("El coche está acelerando.")

    def frenar(self):
        print("El coche está frenando.")

class Bicicleta(Vehiculo):
    def acelerar(self):
        print("La bicicleta está acelerando.")

    def frenar(self):
        print("La bicicleta está frenando.")

# Uso
vehiculos = [Coche(), Bicicleta()]
for v in vehiculos:
    v.acelerar()
    v.frenar()
