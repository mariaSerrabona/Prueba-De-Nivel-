
import clase_vehiculo

class Motocicleta(clase_vehiculo.Vehiculo):
    def __init__(self, color, ruedas, velocidad, cilindrada):
        super().__init__(self, color, ruedas)
        self.velocidad = velocidad
        self.cilindrada = cilindrada

    def __str__(self):
        return super().__str__(self) + ", {} km/h, {}cc".format(self.velocidad, self.cilindrada)