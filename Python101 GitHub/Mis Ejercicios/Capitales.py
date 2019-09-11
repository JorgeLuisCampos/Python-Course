import random

estados_dict = {"Aguascalientes" : "Aguascalientes" , "Baja California" : "Mexicali" , "Baja California Sur" : "La Paz" , 
    "Campeche" : "Campeche" , "Coahuila" : "Saltillo" , "Colima" : "Colima" , "Chiapas" : "Tuxtla Gutiérrez" , 
    "Chihuahua" : "Chihuahua" , "Distrito Federal" : "Ciudad de México" , "Durango" : "Durango" , "Guanajuato" : "Guanajuato" , 
    "Guerrero" : "Chilpancingo" , "Hidalgo" : "Pachuca" , "Jalisco" : "Guadalajara" , "México" : "Toluca" , "Michoacán" : "Morelia" , 
    "Morelos" : "Cuernavaca" , "Nayarit" : "Tepic" , "Nuevo León" : "Monterrey" , "Oaxaca" : "Oaxaca" , "Puebla" : "Puebla" , 
    "Querétaro" : "Querétaro" , "Quintana Roo" : "Chetumal" , "San Luis Potosí" : "San Luis Potosí" , "Sinaloa" : "Culiacán" , 
    "Sonora" : "Hermosillo" , "Tabasco" : "Villahermosa" , "Tamaulipas" : "Ciudad Victoria" , "Tlaxcala" : "Tlaxcala" , 
    "Veracruz" : "Xalapa" , "Yucatán" : "Mérida" , "Zacatecas" : "Zacatecas"}
estados = list(estados_dict)
respuesta = ""

while respuesta != "salir":
    estado = random.choice(estados)
    pregunta = ("Cuál es la capital de " + estado + "?")

    respuesta = input(pregunta)
    if respuesta == "salir":
        print("Gracias por jugar! 👋 ")
        break
    elif respuesta == estados_dict[estado]:
        print ("Correcto! 😊")
    else:
        print("Cerca... pero no! 🙁")



