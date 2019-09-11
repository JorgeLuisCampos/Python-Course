def saludo():
    print("hola")

def saludo2(nombre):
    print("Hola " + nombre)

# si el parámetro tiene asignado un valor, ese valor se usa si no viene nada como parámetro y hace el parámetro opcional
def suma(numeros=[]):   
    total = 0
    for numero in numeros:
        total += numero
    return total
    
def empieza_vocal(palabra):
    if palabra[0] in "aeiouAEIOU":
        return True
    else:
        return False

def nombres_con_vocales(nombres):
    nombres_vocal = []
    for nombre in nombres:
        if nombre[0] in "aeiouAEIOU":
            nombres_vocal.append(nombre)
    
    return nombres_vocal


saludo()
saludo()
saludo2("Juan")

sumar = suma([5, 525, 1.5])
print (sumar)

sumar = suma()
print (sumar)

test = "Juan"
if empieza_vocal (test):
    print (test + " empieza con vocal")

test = "Ana"
if empieza_vocal (test):
    print (test + " empieza con vocal")

nombres_test = ["Hugo", "Eva", "Paco", "Ana", "Omar"]
nombres_resultado = nombres_con_vocales(nombres_test)
print (nombres_resultado)
