# -*- coding: utf-8 -*-
class Ejemplo(object):
    def publico(self):
        print ("Público")

    def __privado(self):
        print ("Privado")

ej = Ejemplo()
ej.publico()
ej.__privado