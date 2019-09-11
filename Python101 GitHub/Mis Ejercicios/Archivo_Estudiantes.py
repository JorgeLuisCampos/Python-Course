archivo = open("./estudiantes.txt", "w")
while True:
    estudiante = input ("Nombre: ")   
    if estudiante == "salir":
        print("Adios!")
        break
    else:
        calificacion = input ("Calificación: ")
        telefono = input("Teléfono:  ")
        archivo.write(estudiante + "," + calificacion + "," + telefono + "\n")

archivo.close()
