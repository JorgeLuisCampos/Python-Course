# -*- coding: utf-8 -*-
import random

class Dado(object):
    def __init__(self, caras):
        self.caras = caras

    def tira(self):
        print("Salió: " + str(random.randint(1,self.caras)))

dado1 = Dado(6)     # dado de 6 caras
dado2 = Dado(24)    # dado de 24 caras

dado1.tira()
dado2.tira()