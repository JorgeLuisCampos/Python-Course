# -*- coding: utf-8 -*-
import random

class Dado(object):
    def __init__(self):
        self.lados = [1,2,3,4,5,6]

    def tira(self):
        print("Salió: " + str(random.choice(self.lados)))

dado1 = Dado()
dado2 = Dado()

dado1.tira()
dado2.tira()