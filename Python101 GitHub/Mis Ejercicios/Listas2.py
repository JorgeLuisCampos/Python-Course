ncv = []
nombres = ["ana", "jorge", "hugo", "paco", "luis", "alberto"]
for nombre in nombres:
    primer_letra = nombre[0]
    resultado = primer_letra in ["a", "e", "i", "o", "u"]
    if resultado == True:
            print(nombre + " inicia con vocal")
            ncv.append(nombre)
print (ncv)