"""""
Ejercicio de herencia múltiple y MRO.

Imagina que estas modelando animales en un zoologico.

Crear 3 clases: "Animal", "Mamifero", "Ave".
La clase animal debe tener un método llamado comer.
La clase mamifero debe tener un metodo llamado amamantar.
La clase ave debe tener un metodo llamado volar.

Ahora, crea una clase llamada "Murcielago" que herede de "Mamifiero" y "Ave"
en ese orden, y por lo tanto debe ser capaz de amamantar y volar, ademas  de comer.

Finalmente, juega con el orden de herencia de la clase "Murcielago" y observa como
cambia el MRO y el comportamiento en los metodos al usar super().
"""""

class Animal:
    def __init__(self, animal):
        self.animal = animal

    def comer(self):
        print(f"El animal {self.animal} esta comiendo.")


class Mamifero(Animal):
    def __init__(self, animal):
        super().__init__(animal)

    def amamantar(self):
        print(f"El animal {self.animal} esta amamantando.")

class Ave(Animal):
    def __init__(self, animal):
        super().__init__(animal)

    def volar(self):
        print(f"El animal {self.animal} esta volando.")


class Murcielago(Mamifero, Ave):
    def __init__(self, animal):
        super().__init__(animal)
    pass


murcielago = Murcielago("Murciélago")

murcielago.comer()

murcielago.amamantar()

murcielago.volar()


ave = Ave("Gaviota")

ave.comer()

ave.volar()

print(Murcielago.mro())
print(Ave.mro())