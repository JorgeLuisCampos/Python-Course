import operator

archivo = open("./Libro/Nariz_Notario.txt", "r")
contador_palabras = {}

for linea in archivo:  
    palabras = linea.split()
    for palabra in palabras:
        if palabra in contador_palabras:
            contador_palabras[palabra] = contador_palabras[palabra] + 1
        else:
            contador_palabras[palabra] = 1

lista_ordenada = {}
resultado = sorted(contador_palabras.items(), key=operator.itemgetter(1))
for item in resultado:
    lista_ordenada[item[0]] = item[1]

#for conteo in contador_palabras:
#    print("La palabra " + conteo + " aparece " + str(contador_palabras[conteo]) + " veces")

for conteo in lista_ordenada:
    print("La palabra " + conteo + " aparece " + str(lista_ordenada[conteo]) + " veces")

#print (contador_palabras)
