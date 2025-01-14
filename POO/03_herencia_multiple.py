class Persona:
    def __init__(self, nombre, edad, nacionalidad):
        self.nombre = nombre
        self.edad = edad
        self.nacionalidad = nacionalidad


    def hablar(self):
        print(f"Hola, mi nombre es {self.nombre} y estoy conversando.")


class Artista:
    def __init__(self, habilidad):
        self.habilidad = habilidad

    def mostrar_habilidad(self):
        return (f"mi habilidad es {self.habilidad}")


    
class EmpleadoArtista(Persona, Artista):
    def __init__(self, nombre, edad, nacionalidad, habilidad, salario, empresa):
        
        Persona.__init__(self, nombre, edad, nacionalidad)
        Artista.__init__(self, habilidad)

        self.salario = salario
        self.empresa = empresa 

    def presentarse(self):
        print(f"Hola, me llamo {self.nombre}, {self.mostrar_habilidad()} y trabajo en {self.empresa}")

roberto = EmpleadoArtista("Roberto", 43, "Argentino", "Cantar", "60.000 mil dls", "Google")
        
roberto.presentarse()