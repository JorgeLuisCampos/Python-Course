# -*- coding: utf-8 -*-
class Terrestre(object):
    def desplazar(self):
        print("El animal anda")

class Acuatico(object):
    def desplazar(self):
        print("El animal nada")

class Cocodrilo(Acuatico, Terrestre): # se va a usar el método de la primera clase declarada cuando exista en una o más. 
    pass


c = Cocodrilo()
c.desplazar()
