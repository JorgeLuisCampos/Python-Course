animals = ['elefante', 'leon', 'tigre', 'jirafa']
print(animals)

animals = animals + ['monkey']
print(animals)

animals += ['dog']
print(animals)

animals.append("dino")
print(animals)

animals[-1] = "dinosaur"
print(animals)

animals.remove('leon')
print(animals)

animals.insert(3, "oso")
print(animals)

birds = ['canario', 'pato']

animals += birds
print(animals)

animals[1:3] = ['cat']
print(animals)

animals[1:3] = []
print(animals)

animals = []   # Otras opciones: animals.clear() y animals[:] = []
print(animals)
