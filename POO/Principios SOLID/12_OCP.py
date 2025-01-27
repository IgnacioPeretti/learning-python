"""""
OCP - (Open/Closed Principle - OCP) - Principio de Abierto/Cerrado

Las clases deben estar abiertas para su extensión, pero cerradas para su modificación.

Se refiere a que puedes agregar nuevas funcionalidades a una clase sin necesidad de modificar el código existente.
Esto se logra con la herencia o interfaces.

Ejemplo:  En lugar de modificar una clase para agregar una nueva funcionalidad,
utiliza la herencia o la composición para extender su comportamiento.
"""""

class Notificador:
    def __init__(self, usuario, mensaje):

        self.usuario = usuario
        self.mensaje = mensaje

    def notificar(self):
        raise NotImplementedError

class NotificacionEmail(Notificador):
    def Notificar(self):
        print(f"Enviando mensaje por Email a {self.usuario.email}")

class NotificacionSMS(Notificador):
    def Notificar(self):
        print(f"Enviando mensaje por SMS a {self.usuario.sms}")

class NotificacionWhatsapp(Notificador):
    def Notificar(self):
        print(f"Enviando mensaje por whatsapp a {self.usuario.whatsapp}")
        