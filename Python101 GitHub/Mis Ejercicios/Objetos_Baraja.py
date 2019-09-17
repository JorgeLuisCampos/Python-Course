# -*- coding: utf-8 -*-
import random

class Baraja(object):
    def __init__(self):
        self.palos = ["Espadas", "Corazones", "Tréboles", "Diamantes"]
        self.rangos = ["2", "3", "4", "5", "6", "7", "8", "9", "10", "Jack", "Queen", "King", "As"]
        self.maso = []

        for palo in self.palos:
            for rango in self.rangos:
                self.maso.append(rango + " de " + palo)

    def barajear(self):
        random.shuffle(self.maso)

    def repartir(self):
        print(self.maso.pop())
        # self.maso.pop(0)

""" 
Usando (instanciando) el objeto
"""
baraja = Baraja()
baraja.barajear()
baraja.repartir()
baraja.repartir()
baraja.repartir()
baraja.repartir()
baraja.repartir()



