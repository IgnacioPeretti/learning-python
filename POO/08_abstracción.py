"""""
 Su propósito principal es manejar la complejidad del sistema ocultando detalles innecesarios 
 y mostrando solo la información esencial relevante para el problema que se desea resolver.

 En POO, la abstracción consiste en: 

 - Definir clases enfocándose únicamente en las características esenciales.
 - Ocultar los detalles de implementación interna, presentando solo lo necesario para interactuar con el objeto.

"""""


class Auto:
    def __init__(self):
        self.estado = "apagado"

    def encender(self):
        self.estado = "Encendido"
        print("El auto esta encendido.")
    
    def conducir(self):
        if self.estado == "apagado":
            self.encender()
        print("Conduciendo el auto.")

mi_auto = Auto()

mi_auto.conducir()