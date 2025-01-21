"""""
ISP - Interface Segregation Principle (Principio de Segregación de Interfaces)

Una clase no debe verse obligada a implementar interfaces que no usa.
Evitar interfaces grandes y monolíticas dividiéndolas en interfaces más específicas.

Ejemplo: En lugar de una interfaz Animal con métodos como volar(), nadar() y caminar(),
divide la interfaz en Volador, Nadador y Caminador, implementando solo lo necesario.
"""""


from abc import ABC, abstractmethod

class Trabajador(ABC):

    @abstractmethod
    def trabajar(self):
        pass

class Durmiente(ABC):

    @abstractmethod
    def dormir(self):
        pass

class Comedor(ABC):

    @abstractmethod
    def comer(self):
        pass

class Humano(Trabajador, Durmiente, Comedor):
    def comer(self):
        print("El humano esta comiendo.")
    
    def dormir(self):
        print("El humano esta durmiendo.")

    def trabajar(self):
        print("El humano esta trabajando.")


class Robot(Trabajador):
    def trabajar(self):
        print("El robot esta trabajando.")



robot = Robot()

robot.trabajar()


humano = Humano()

humano.comer()
humano.dormir()
humano.trabajar()