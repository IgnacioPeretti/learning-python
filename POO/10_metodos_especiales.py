"""""
Estos métodos permiten redefinir cómo los objetos interactúan con las funciones y operadores integrados de Python.
Su nombre comienza y termina con doble guion bajo (__).

Ventajas de los métodos especiales: 

- Flexibilidad: Personalizas completamente cómo se comportan tus objetos.
- Intuitivo: Permite que los objetos se usen como si fueran tipos nativos de Python.
- Reutilización: Los métodos mágicos se integran con muchas funciones integradas (len(), sorted(), str()).

"""""

# __init__ Se ejecuta cuando se crea una instancia de la clase. Sirve para inicializar atributos.

class Persona:
    def __init__(self, nombre, edad):
        self.nombre = nombre
        self.edad = edad


# __str__(self): Devuelve una representación "amigable" del objeto, útil para print.

class Persona:
    def __str__(self):
        return f"{self.nombre}, {self.edad} años"

# __repr__(self): Proporciona una representación formal del objeto para depuración.

class Persona:
    def __repr__(self):
        return f"Persona(nombre={self.nombre}, edad={self.edad})"
