archivo = open("./paises.txt", "r")
paises = []
for linea in archivo:
    paises.append(linea.strip())

for pais in paises:
    print(pais)

print ("Total de Países: " + str(len(paises)))

for pais in paises:
    if pais[0] == "M":
        print("País con M: " + pais)

#print(paises)

archivo.close()