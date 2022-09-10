#clase que representa a los objeto de tipo camioneta

import clase_vehiculo

class Camioneta(clase_vehiculo.Vehiculo):
    def __init__(self, color, ruedas, carga):
        clase_vehiculo.Vehiculo.__init__(self, color, ruedas)
        self.carga = carga

    def __str__(self):
        return clase_vehiculo.Vehiculo.__str__(self) + ", {} kg".format(self.carga)