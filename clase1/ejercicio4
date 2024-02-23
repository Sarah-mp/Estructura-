class Vehiculo:
    def __init__(self, tipo, nivel_combustible):
        self.tipo = tipo
        self.nivel_combustible = nivel_combustible

    def encender(self):
        if self.nivel_combustible < 0.1:  # 10% del nivel de combustible
            print("Advertencia: Nivel de combustible bajo. Por favor, diríjase a la gasolinera.")
        else:
            print("Vehículo encendido.")


class Carro(Vehiculo):
    def __init__(self, marca, modelo, cilindrada, nivel_combustible):
        super().__init__("Carro", nivel_combustible)
        self.marca = marca
        self.modelo = modelo
        self.cilindrada = cilindrada


class Moto(Vehiculo):
    def __init__(self, marca, modelo, cilindrada, nivel_combustible):
        super().__init__("Moto", nivel_combustible)
        self.marca = marca
        self.modelo = modelo
        self.cilindrada = cilindrada


# Crear instancias de las clases Carro y Moto con diferentes niveles de combustible
mi_carro = Carro("Toyota", "Corolla", "1600cc", 0.05)  # Nivel bajo de combustible
mi_moto = Moto("Honda", "CBR500R", "500cc", 0.2)  # Nivel suficiente de combustible

# Probar el método encender para cada vehículo
mi_carro.encender()  # Debería mostrar la advertencia
mi_moto.encender()  # Debería encender el vehículo
