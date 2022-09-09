class Vehiculo():
    def __init__(self, color, ruedas):
        self.color = color
        self.ruedas = ruedas
def __str__(self):
    return "Color {}, {} ruedas".format( self.color, self.ruedas )

class Coche(Vehiculo):
    def __init__(self, color, ruedas, velocidad, cilindrada): Vehiculo.__init__(self, color, ruedas)
        self.velocidad = velocidad
        self.cilindrada = cilindrada

    def __str__(self):
        return Vehiculo.__str__(self) + ", {} km/h, {}cc".format(self.velocidad, self.cilindrada)


class Camioneta(Vehiculo):
    def __init__(self, color, ruedas, carga): Vehiculo.__init__(self, color, ruedas)
        self.carga = carga

    def __str__(self):
        return Vehiculo.__str__(self) + ", {} km/h, {}cc".format(self.carga)


coche1 = Coche("azul", 4, 150, 1200)

print(coche)
