
import clase_vehiculo

class Bicicleta(clase_vehiculo.Vehiculo):
    def __init__(self, color, ruedas, tipo):
        clase_vehiculo.Vehiculo.__init__(self, color, ruedas)
        self.tipo = tipo

    def __str__(self):
        return clase_vehiculo.Vehiculo.__str__(self) + ", {}".format(self.tipo)