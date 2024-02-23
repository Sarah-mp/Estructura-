class Vehiculo:
    def __init__(self, marca, modelo):
        self.marca = marca
        self.modelo = modelo

    def __str__(self):
        return f"{self.marca} {self.modelo}"

class Moto(Vehiculo):
    def __init__(self, marca, modelo, cilindraje):
        super().__init__(marca, modelo)
        self.cilindraje = cilindraje

    def __str__(self):
        return f"Moto: {self.marca} {self.modelo}, Cilindraje: {self.cilindraje}"

class Carro(Vehiculo):
    def __init__(self, marca, modelo, color):
        super().__init__(marca, modelo)
        self.color = color

    def __str__(self):
        return f"Carro: {self.marca} {self.modelo}, Color: {self.color}"

# Crear instancias de las nuevas clases
mi_moto = Moto("Honda", "CBR500R", "500cc")
mi_carro = Carro("Toyota", "Corolla", "Blanco")

# Imprimir los objetos instanciados
print(mi_moto)
print(mi_carro)
