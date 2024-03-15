class Vehiculo:
    def __init__(self, tipo, nivel_combustible):
        self.tipo = tipo
        self.nivel_combustible = nivel_combustible

    def encender(self):
        if self.nivel_combustible < 0.1:
            print("Advertencia: Nivel de combustible bajo. Por favor, diríjase a la gasolinera.")
        else:
            print("Vehículo encendido.")

    def marchar(self, distancia):
        consumo_combustible = 0.05  # Consumo de combustible por kilómetro (puedes ajustar este valor)
        combustible_consumido = consumo_combustible * distancia
        self.nivel_combustible -= combustible_consumido

        if self.nivel_combustible <= 0:
            print("El vehículo se ha quedado sin combustible. Deteniendo la marcha.")
            self.nivel_combustible = 0
        elif self.nivel_combustible < 0.1:
            print("Advertencia: Nivel de combustible bajo. Por favor, diríjase a la gasolinera.")
        else:
            print(f"El vehículo ha recorrido {distancia} kilómetros. Nivel de combustible restante: {self.nivel_combustible}")


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
mi_carro = Carro("Toyota", "Corolla", "1600cc", 0.5)  # Nivel suficiente de combustible
mi_moto = Moto("Honda", "CBR500R", "500cc", 0.2)  # Nivel suficiente de combustible

# Probar el método marchar() para cada vehículo
mi_carro.encender()
mi_carro.marchar(50)  # Simular recorrido de 50 km
print()
mi_moto.encender()
mi_moto.marchar(30)  # Simular recorrido de 30 km
