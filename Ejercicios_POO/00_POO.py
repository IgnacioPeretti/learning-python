"""""
Crear una clase estudiante con los atributos Nombre, Edad y Grado ademas
agregar un método que se llame Estudiar y que imprima un mensaje sobre el 
estudiante.

Crear una instancia de la clase y usar el método pero para ello debemos generar
una interacción con el usuario el cual debe brindar los atributos.
"""""


class Estudiante:
    def __init__(self, Nombre, Edad, Grado):

        self.nombre = Nombre
        self.edad = Edad
        self.grado = Grado

    def estudiar(self):
        print(f"El estudiante {self.nombre} esta estudiando.")


nombre = input("Ingrese el nombre del estudiante: ")
edad = input("Ingrese la edad del estudiante: ")
grado = input("Ingrese el grado del estudiante: ")

estudiante1 = Estudiante(nombre, edad, grado)

print(f"""
      Datos del estudiante. \n
      Nombre: {estudiante1.nombre} \n
      Edad: {estudiante1.edad} \n
      Grado: {estudiante1.grado} \n
                        """)


estudiar = input()

if estudiar.lower() == "estudiar":
    estudiante1.estudiar()

         
