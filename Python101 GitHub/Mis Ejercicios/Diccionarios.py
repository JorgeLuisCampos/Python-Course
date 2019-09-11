# Los diccionarios son como las listas, pero tienen nombres de campos y es entre llaves
# Crear nuevo Diccionario
phone_book = {"John": 123, "Jane": 234, "Jerard": 345}
print(phone_book)

# Agregar un nuevo elemento al diccionario
phone_book["Jill"] = 456
print(phone_book)

# Remove key-value pair from phone_book
del phone_book['John']
print(phone_book)

print(phone_book['Jane'])
print(phone_book.keys())   # Imprime solo las llaves
print(phone_book.values()) # Imprime solo los valores

name_list = phone_book.keys()
print(name_list)
print(type(name_list))

