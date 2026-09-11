def obtener_clase(clase):
    if clase == 1:
        return "barbaro"
    elif clase == 2:
        return "guerrero"
    elif clase == 3:
        return "bardo"
    else:
        return "mago"


def obtener_hp(clase):
    if clase == 1:
        return 30
    elif clase == 2:
        return 25
    elif clase == 3:
        return 20
    else:
        return 15


nombre = input("Escribe el nombre de tu personaje: ")

print("")
print("Elige una clase:")
print("1. Barbaro")
print("2. Guerrero")
print("3. Bardo")
print("4. Mago")

clase = int(input("Escribe el número de la clase: "))

nombre_clase = obtener_clase(clase)
hp = obtener_hp(clase)

print("")
print("--- PERSONAJE CREADO ---")
print("Nombre:", nombre)
print("Clase:", nombre_clase)
print("HP:", hp)
