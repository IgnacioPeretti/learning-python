# Metodos

class Celular:                # Clase
    def __init__(self, marca, modelo, camara):           # Metodo constructor

        self.marca = marca
        self.modelo = modelo               # Atributos
        self.camara = camara

    def llamar(self):                                                      # Metodos
        print(f"Estas haciendo un llamado desde un: {self.modelo}")

    def cortar(self): 
        print(f"Cortaste la llamada desde tu: {self.modelo}")
    
    def atender(self):
        print(f"Atendiste un llamado desde tu: {self.modelo}")

celular1 = Celular("Apple", " Iphone 13 PRO", "60MP")
celular2 = Celular("Samsumg", "S23", "50MP")


celular1.llamar()

celular2.atender()

celular2.cortar()
