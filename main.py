
import clase_coche

import clase_camioneta

import clase_bicicleta
import clase_motocicleta


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


def catalogar2(ruedas_pedidas, lista):

    vehiculos_ruedas=0
    for vehiculo in lista:
        if vehiculo.ruedas==ruedas_pedidas:
            vehiculos_ruedas+=1
            print(lista[lista.index(vehiculo)])

    print('Se han encontrado '+ str(vehiculos_ruedas)+' coches con '+ str(ruedas_pedidas)+ ' ruedas')



if __name__ == "__main__":


    coche1 = clase_coche.Coche("azul", 4, 150, 1200)
    camioneta1=clase_camioneta.Camioneta('verde', 4, 1900)
    bicicleta1=clase_bicicleta.Bicicleta('amarilla', 2, 'deportiva')
    motocicleta1=clase_motocicleta.Motocicleta('marron', 2, 300, 1100)

    print(coche1)

    print(camioneta1)

    print(bicicleta1)

    print(motocicleta1)

    lista_vehiculos = [coche1, camioneta1, bicicleta1, motocicleta1]


    catalogar(lista_vehiculos)


    catalogar2(0, lista_vehiculos)



