
class Vehiculo():
    def __init__(self, color, ruedas):
        self.color = color
        self.ruedas = ruedas
    def __str__(self):
        return "Color {}, {} ruedas".format( self.color, self.ruedas )

class Coche(Vehiculo):
    def __init__(self, color, ruedas, velocidad, cilindrada):
        Vehiculo.__init__(self, color, ruedas)
        self.velocidad = velocidad
        self.cilindrada = cilindrada

    def __str__(self):
        return Vehiculo.__str__(self) + ", {} km/h, {}cc".format(self.velocidad, self.cilindrada)


class Camioneta(Vehiculo):
    def __init__(self, color, ruedas, carga):
        Vehiculo.__init__(self, color, ruedas)
        self.carga = carga

    def __str__(self):
        return Vehiculo.__str__(self) + ", {} kg".format(self.carga)


class Bicicleta(Vehiculo):
    def __init__(self, color, ruedas, tipo):
        Vehiculo.__init__(self, color, ruedas)
        self.tipo = tipo

    def __str__(self):
        return Vehiculo.__str__(self) + ", {}".format(self.tipo)


class Motocicleta(Vehiculo):
    def __init__(self, color, ruedas, velocidad, cilindrada):
        Vehiculo.__init__(self, color, ruedas)
        self.velocidad = velocidad
        self.cilindrada = cilindrada

    def __str__(self):
        return Vehiculo.__str__(self) + ", {} km/h, {}cc".format(self.velocidad, self.cilindrada)


coche1 = Coche("azul", 4, 150, 1200)
camioneta1=Camioneta('verde', 4, 1900)
bicicleta1=Bicicleta('amarilla', 2, 'deportiva')
motocicleta1=Motocicleta('marron', 2, 300, 1100)

print(coche1)

# print(camioneta1)

# print(bicicleta1)

# print(motocicleta1)

lista_vehiculos = [coche1, camioneta1, bicicleta1, motocicleta1]


def catalogar(lista):
    for vehiculo in lista:

        print(type(vehiculo).__name__)
        print(vehiculo.color)
        print (vehiculo.ruedas)

        if type(vehiculo).__name__=='Coche':
            print(vehiculo.velocidad)
            print(vehiculo.cilindrada)


        if type(vehiculo).__name__=='Motocicleta':
            print(vehiculo.velocidad)
            print(vehiculo.cilindrada)

        if type(vehiculo).__name__=='Bicicleta':
            print(vehiculo.tipo)

        if type(vehiculo).__name__=='Camioneta':
            print(vehiculo.carga)


catalogar(lista_vehiculos)



def catalogar2(ruedas_pedidas, lista):

    vehiculos_ruedas=0
    for vehiculo in lista:
        if vehiculo.ruedas==ruedas_pedidas:
            vehiculos_ruedas+=1

    print(vehiculos_ruedas)


catalogar2(4, lista_vehiculos)



