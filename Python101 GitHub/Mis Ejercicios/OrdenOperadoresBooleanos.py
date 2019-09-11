# No se evaluan de izquierda a derecha:
# Not se evalua primero, And se evalua despues y Or al final

name = "John"
age = 17

print(name == "John" or not age > 17)

print(name == "John" and not age > 17)

print(name == "Ellis" or not (name == "John" and age == 17))

