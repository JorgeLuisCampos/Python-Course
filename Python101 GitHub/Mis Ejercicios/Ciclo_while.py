contador = 0
while contador < 5:
    print ("Hola " + str(contador))
    contador += 1


contador = 0
while contador < 50:
    print ("Hola " + str(contador))
    contador += 1
    if contador > 10:
            break


While True:
    opcion = input("> ")
    if opcion == "salir":
        break

while True:
    opcion = input ("> ")
    if opcion == "salir":
            print("Adios")
            break
   else:
            print(opcion)