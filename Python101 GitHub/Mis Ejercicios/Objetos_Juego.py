# -*- coding: utf-8 -*-
import random

class Juego(object):
    def __init__(self, jugadores):
        self.jugadores = jugadores
        self.players = []
        self.activos = 0
        for jugador in self.jugadores:
            self.players.append(Player(jugador))
            self.activos += 1

    def turno(self):
        self.activos = 0
        for jugador in self.jugadores:
            indice = self.jugadores.index(jugador)
            print ("Jugador " + str(indice) + ": " + jugador)
            if self.players[indice].vida > 0:
                if random.randint(0,1) == 0:    # pierde energía
                    self.players[indice].take_damage()
                else:                           # gana energia
                    self.players[indice].powerup()
                if self.players[indice].vida > 0:
                    self.activos += 1 
            else:
                print ("Jugador " + str(indice) + ": " + jugador + " ya no juega")

class Player(object):
    def __init__(self, nombre):
        self.vida = random.randint(0,50)
        self.nombre = nombre
        self.health()

    def powerup(self):
        incremento = random.randint(1,10)
        print (self.nombre + " recibió " + str(incremento) + " energia")
        self.vida += incremento
        self.health()
        # print ("La energía de " + self.nombre + " es " + str(self.vida))
        
    def take_damage(self):
        decremento = random.randint(1,10)
        print (self.nombre + " perdió " + str(decremento) + " energia")
        self.vida -= decremento
        if self.vida <= 0:
            print ("Game Over " + self.nombre)
        else:
            self.health()
            # print ("La energía de " + self.nombre + " es " + str(self.vida))

    def health(self):
        print ("La energía de " + self.nombre + " es " + str(self.vida))


mijuego = Juego(["Juan", "Pedro", "Luis"])
while mijuego.activos > 1:
    mijuego.turno()

for jugador in mijuego.players:
    if jugador.vida > 0:
        print ("El ganador es " + jugador.nombre + " con " + str(jugador.vida) + " energía")


