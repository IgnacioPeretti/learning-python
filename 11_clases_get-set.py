### Clases ###


"""""
Una clase es una estructura que define un tipo de objeto.
Es un plano o plantilla que describe las características y comportamientos comunes que comparten los objetos de ese tipo.
"""""
"""""
Los getters y setters son métodos utilizados para acceder y modificar los valores de los atributos (o propiedades) de un objeto.
Ayudan a controlar el acceso a los datos de una clase, protegiendo la integridad de los mismos.

Getters: Permiten obtener (leer) el valor de un atributo de una clase de manera controlada.
Setters: Permiten modificar (escribir) el valor de un atributo de una clase de manera controlada.

"""""



class Person:
    def __init__(self, name, surname, age):  
        self.full_name = f"{name} {surname} {age}" 
        self._name = name                                       # Variables privadas
        self._surname = surname
        self._age = age
        
    
    def get_name(self):
        return self._name
    
    def set_name(self, name):
        self._name = name

    def get_surname(self):
        return self._surname
    
    def set_surname(self, surname):
        self._surname

    def get_age(self):
        return self._age
    
    def set_age(self, age):
        if age < 0:
            print("La edad no puede ser negativa.")
        else:
            self._age = age

    def walk(self):                                    # Funcion dentro de una clase
        print(f"{self.full_name} Esta caminando")
    
    def correr(self):
        print(f"{self.full_name} Esta corriendo")
        

my_person = Person("Ignacio", "Peretti", 24)   # Defino una persona con una función 
print(my_person.full_name)
my_person.walk()

print("Uso de los getters y setters")

my_person2 = Person("Pedro", "Peretti", 27)


print(my_person2.get_name())
print(my_person2.get_surname())
print(my_person2.get_age())

my_person2.set_age(30)                      # Le asigno otra age usando el setter
print(my_person2.get_age())

my_person2.set_age(-5)
print(my_person2.get_age())                 # Comprobamos que el setter funcione

my_person2.set_name("Carlos")
print(my_person2.get_name())


"""""
Resumen:
Los getters son métodos para obtener los valores de los atributos privados.
Los setters son métodos para modificar los valores de los atributos privados.

Usar getters y setters te permite controlar cómo accedes y modificas los atributos internos de la clase, 
en lugar de hacerlo directamente, lo que puede mejorar la seguridad y mantenibilidad del código.

"""""