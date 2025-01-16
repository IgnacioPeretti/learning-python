class Gato:
    def sonido(self):
        return "Miau"


class Perro:
    def sonido(self):
        return "Guau"
    
    
def hacersonido(animal):
    print(animal.sonido())

gato = Gato()

perro = Perro()

hacersonido(perro)

print(gato.sonido())