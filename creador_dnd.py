import random


def obtener_clase(clase):
    if clase == 1:
        return "Guerrero"
    elif clase == 2:
        return "Mago"
    elif clase == 3:
        return "Barbaro"
    else:
        return "Bardo"


def obtener_hp(clase):
    if clase == 1:
        return 25
    elif clase == 2:
        return 15
    elif clase == 3:
        return 30
    else:
        return 20


def obtener_raza(raza):
    if raza == 1:
        return "Humano"
    elif raza == 2:
        return "Elfo"
    elif raza == 3:
        return "Enano"
    else:
        return "Orco"


# Diccionario para guardar personajes
personajes_guardados = {}
contador = 0

opcion = 0

while opcion == 0:

    print("")
    print("===== GENERADOR DE PERSONAJES DND =====")
    print("1. Crear nuevo personaje")
    print("2. Ver personajes guardados")
    print("3. Salir")

    opcion = int(input("Elige una opcion: "))

    if opcion == 1:

        nombre = input("Escribe el nombre de tu personaje: ")

        print("")
        print("Elige una raza:")
        print("1. Humano")
        print("2. Elfo")
        print("3. Enano")
        print("4. Orco")

        raza = int(input("Escribe el numero de la raza: "))

        print("")
        print("Elige una clase:")
        print("1. Guerrero")
        print("2. Mago")
        print("3. Barbaro")
        print("4. Bardo")

        clase = int(input("Escribe el numero de la clase: "))

        nombre_raza = obtener_raza(raza)
        nombre_clase = obtener_clase(clase)
        hp = obtener_hp(clase)

        descripcion = input("Escribe una descripcion de tu personaje: ")

        # Estadisticas aleatorias
        # Autoestudio: modulo random de Python
        fuerza = random.randint(1, 20)
        inteligencia = random.randint(1, 20)
        agilidad = random.randint(1, 20)

        # Bonificaciones por clase
        if clase == 1:
            fuerza = fuerza + 3

        elif clase == 2:
            inteligencia = inteligencia + 5

        elif clase == 3:
            fuerza = fuerza + 5

        else:
            agilidad = agilidad + 3

        # Limite maximo de atributos
        if fuerza > 20:
            fuerza = 20

        if inteligencia > 20:
            inteligencia = 20

        if agilidad > 20:
            agilidad = 20

        # Crear diccionario del personaje
        personaje = {
            "nombre": nombre,
            "raza": nombre_raza,
            "clase": nombre_clase,
            "fuerza": fuerza,
            "inteligencia": inteligencia,
            "agilidad": agilidad,
            "hp": hp,
            "descripcion": descripcion
        }

        # Guardar personaje
        contador = contador + 1
        personajes_guardados[contador] = personaje

        print("")
        print("----- PERSONAJE CREADO -----")
        print("Nombre:", personaje["nombre"])
        print("Raza:", personaje["raza"])
        print("Clase:", personaje["clase"])
        print("Fuerza:", personaje["fuerza"])
        print("Inteligencia:", personaje["inteligencia"])
        print("Agilidad:", personaje["agilidad"])
        print("HP:", personaje["hp"])
        print("Descripcion:", personaje["descripcion"])

        opcion = 0

    elif opcion == 2:

        print("")
        print("===== PERSONAJES GUARDADOS =====")

        if contador == 0:
            print("Todavia no hay personajes guardados.")

        else:
            for numero in personajes_guardados:

                personaje = personajes_guardados[numero]

                print("")
                print("Personaje numero:", numero)
                print("Nombre:", personaje["nombre"])
                print("Raza:", personaje["raza"])
                print("Clase:", personaje["clase"])
                print("Fuerza:", personaje["fuerza"])
                print("Inteligencia:", personaje["inteligencia"])
                print("Agilidad:", personaje["agilidad"])
                print("HP:", personaje["hp"])
                print("Descripcion:", personaje["descripcion"])

        opcion = 0

    elif opcion == 3:

        print("")
        print("Gracias por usar el generador de personajes DND :)")
        print("Hasta luego!")

    else:

        print("")
        print("Opcion incorrecta.")

        opcion = 0
