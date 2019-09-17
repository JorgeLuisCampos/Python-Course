# -*- coding: utf-8 -*-
class Coche(object):
    #Abstracción de los objetos coche.
    def __init__(self, gasolina):
        self.gasolina = gasolina
        print ("Tenemos " + str(gasolina) + " litros")

    def arrancar(self):
        if self.gasolina > 0:
            print ("Arranca")
        else:
            print ("No arranca")

    def conducir(self):
        if self.gasolina > 0:
            self.gasolina -= 1
            print ("Quedan " + str(self.gasolina) + " litros")
        else:
            print ("No se mueve")


micoche = Coche(5)
micoche.arrancar()
micoche.conducir()
micoche.conducir()
micoche.conducir()
micoche.conducir()
micoche.conducir()
micoche.conducir()
micoche.conducir()
micoche.arrancar()
