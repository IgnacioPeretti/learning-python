class Celular:                # Clase
    def __init__(self, marca, modelo, camara):           # Metodo constructor

        self.marca = marca
        self.modelo = modelo               # Atributos
        self.camara = camara


celular1 = Celular("Apple", "13 PRO", "60MP")

print(celular1.marca, celular1.modelo, celular1.camara)