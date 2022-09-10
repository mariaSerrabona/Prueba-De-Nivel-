
#segunda clase que define a  los objetos de tipo coche

import clase_vehiculo

class Coche(clase_vehiculo.Vehiculo):
    def __init__(self, color, ruedas, velocidad, cilindrada):
        clase_vehiculo.Vehiculo.__init__(self, color, ruedas)
        self.velocidad = velocidad
        self.cilindrada = cilindrada

    def __str__(self):
        return clase_vehiculo.Vehiculo.__str__(self) + ", {} km/h, {}cc".format(self.velocidad, self.cilindrada)