class Persona:
    def __init__(self, nombre, edad, nacionalidad):
        self.nombre = nombre
        self.edad = edad
        self.nacionalidad = nacionalidad
    def hablar(self):
        print(f"Hola, mi nombre es {self.nombre} y estoy conversando.")

class Empleado(Persona):
    def __init__(self, nombre, edad, nacionalidad, trabajo, salario):
        super().__init__(nombre, edad, nacionalidad)
        self.trabajo = trabajo
        self.salario = salario

    

roberto = Empleado("Roberto", 43, "Argentino", "Programador", "60.000 dls")


roberto.hablar()

print(roberto.nombre, roberto.trabajo, roberto.salario)
        