"""""
DIP - Dependency Inversion Principle (Principio de Inversión de Dependencias)

Los módulos de alto nivel no deben depender de los módulos de bajo nivel. Ambos deben depender de abstracciones.

Reducir el acoplamiento directo entre clases al depender de interfaces o abstracciones,
facilitando el cambio y la escalabilidad.

Ejemplo: En lugar de que una clase dependa directamente de otra clase concreta,
utiliza interfaces para que la dependencia sea genérica y flexible.
"""""       
 
# Asi sería un caso que viole este principio

# class Diccionario:
#     def verificar_palabra(self):
#         # Lógica para verificar palabras
#         pass

# class CorrectorOrtografico:
#     def __init__(self):
#         self.diccionario = Diccionario()

#     def corregir_texto(self, texto):
#         # usamos el diccionario para corregir el texto 


from abc import ABC, abstractmethod

class VerficadorOrtografico(ABC):
    @abstractmethod
    def verificar_palabra(self, palabra):
        pass

class Diccionario(VerficadorOrtografico):
    def verificar_palabra(self, palabra):
        # Lógica para verficar palabra
        pass

class CorrectorOrtografico:
    def __init__(self, verificador):
        self.verificador = verificador

    def corregir_texto(self, texto):
        # Usamos el verificador para corregir texto
        pass

corrector = CorrectorOrtografico()