class Vehiculo:
    def __init__(self, tipo):
        self.tipo = tipo

class Carro(Vehiculo):
    def __init__(self, marca, modelo, cilindrada):
        super().__init__("Carro")
        self.marca = marca
        self.modelo = modelo
        self.cilindrada = cilindrada

    def __str__(self):
        return f"Tipo: {self.tipo}, Marca: {self.marca}, Modelo: {self.modelo}, Cilindrada: {self.cilindrada}"

class Moto(Vehiculo):
    def __init__(self, marca, modelo, cilindrada):
        super().__init__("Moto")
        self.marca = marca
        self.modelo = modelo
        self.cilindrada = cilindrada

    def __str__(self):
        return f"Tipo: {self.tipo}, Marca: {self.marca}, Modelo: {self.modelo}, Cilindrada: {self.cilindrada}"

# Crear instancias de las clases Carro y Moto
mi_carro = Carro("Toyota", "Corolla", "1600cc")
mi_moto = Moto("Honda", "CBR500R", "500cc")

# Imprimir los objetos instanciados
print(mi_carro)
print(mi_moto)
