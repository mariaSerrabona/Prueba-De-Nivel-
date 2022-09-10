
import clase_vehiculo
import clase_coche

import clase_camioneta






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



