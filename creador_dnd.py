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
        print("Elige una clase:")
        print("1. Guerrero")
        print("2. Mago")
        print("3. Barbaro")
        print("4. Bardo")

        clase = int(input("Escribe el numero de la clase: "))

        nombre_clase = obtener_clase(clase)
        hp = obtener_hp(clase)

        fuerza = 10
        inteligencia = 10
        agilidad = 10

        if clase == 1:
            fuerza = fuerza + 3

        elif clase == 2:
            inteligencia = inteligencia + 5

        elif clase == 3:
            fuerza = fuerza + 5

        else:
            agilidad = agilidad + 3

        print("")
        print("----- PERSONAJE CREADO -----")
        print("Nombre:", nombre)
        print("Clase:", nombre_clase)
        print("Fuerza:", fuerza)
        print("Inteligencia:", inteligencia)
        print("Agilidad:", agilidad)
        print("HP:", hp)

        opcion = 0

    elif opcion == 2:

        print("")
        print("Esta opcion se agregara mas adelante.")

        opcion = 0

    elif opcion == 3:

        print("")
        print("Gracias por usar el generador de personajes DND :)")
        print("Hasta luego!")

    else:

        print("")
        print("Opcion incorrecta.")

        opcion = 0
