class Persona(object):
    def __init__(self, nombre): # Constructor
        nombre = nombre.title() # Convierte la primera letra en mayúsculas y el resto en minúsculas
        self.nombre = nombre

    def saluda(self):
        print("Hola, soy " + self.nombre)

    def despidete(self):
        print("Adios, se despide " + self.nombre)

juan = Persona("JUAN")
pedro = Persona("pEdro")

juan.saluda()
pedro.despidete()
