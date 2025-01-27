"""""
LSP - Liskov Substitution Principle (Principio de Sustitución de Liskov)

Las clases derivadas deben ser sustituibles por sus clases base sin alterar 
el correcto funcionamiento del programa.

Garantizar que el código que usa una clase base pueda trabajar con cualquier subclase sin problemas.

Ejemplo: Si tienes una clase Ave con un método volar(), todas las subclases (como Pinguino o Hálcon)
deben poder usarse de manera intercambiable sin cambiar la lógica del cliente.

Esto sucede porque no todas las subclases de Ave pueden volar, lo que rompe la expectativa
del cliente que utiliza el método volar()
"""""


class Ave:
    pass


class AveVoladora(Ave):
    def volar(self):
        return "Estoy volando"
    
class AveNoVoladora(Ave):
    pass
