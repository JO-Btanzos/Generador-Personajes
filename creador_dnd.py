#esto es para que phyton pueda usar la librería random, que es para
#los numeros aleatorios

import random

opcion = ""

#aqui es para que mientras la opcion no sea 3 (salir),
#se ejecute el resto del código

while opcion != "3":

    print("=== GENERADOR DE PERSONAJES ===")
    print("1. Crear personaje")
    print("2. Ver personajes")
    print("3. Salir")

    opcion = input("Elige una opción: ")
    
#esto es cuando se elige 1 (crear personaje)

    if opcion == "1":

        nombre = input("Escribe el nombre de tu personaje: ")

        clase = ""

#esto es por si elige una clase que no sea 1, 2, 3 o 4

        while clase != "1" and clase != "2" and clase != "3" and clase != "4":

#aqui ya elije la clase

            print("")
            print("Elige una clase:")
            print("1. Bárbaro")
            print("2. Guerrero")
            print("3. Bardo")
            print("4. Mago")

            clase = input("Escribe el número de la clase: ")
            
#esto es por si no eligío 1,2,3 o 4.
#Cuando eso pasa entonces muestra un mensaje de error

            if clase != "1" and clase != "2" and clase != "3" and clase != "4":

                print("")
                print("Error. Debes elegir una clase correcta.")
                print("Elige un número del 1 al 4.")
                
#aquí usa lo de random para las stats,
#lo de randit es para que elija un número
#entero de entre los que estan en el parentesis

        fuerza = random.randint(1, 20)
        inteligencia = random.randint(1, 20)
        agilidad = random.randint(1, 20)

#esto es lo que agregará a cada clase

        if clase == "1":

            nombre_clase = "Bárbaro"
            fuerza = fuerza + 5
            hp = 30

        elif clase == "2":

            nombre_clase = "Guerrero"
            fuerza = fuerza + 3
            hp = 25

        elif clase == "3":

            nombre_clase = "Bardo"
            agilidad = agilidad + 3
            hp = 20

        elif clase == "4":

            nombre_clase = "Mago"
            inteligencia = inteligencia + 5
            hp = 15

#aqui ya muestra tu personaje creado con todas sus stats

        print("")
        print("--- PERSONAJE CREADO ---")
        print("Nombre:", nombre)
        print("Clase:", nombre_clase)
        print("HP:", hp)
        print("Fuerza:", fuerza)
        print("Inteligencia:", inteligencia)
        print("Agilidad:", agilidad)
        print("")
        
#esto abre un archivo llamado personajes.txt
#y lo hace en agregar ("a"), y si no hay tal archivo, lo crea,
#además lo guarda en la variable archivo

        archivo = open("personajes_dnd.txt", "a")
    
#esto es lo que va a meter en ese archivo

        archivo.write("Nombre: " + nombre + "\n")
        archivo.write("Clase: " + nombre_clase + "\n")
        archivo.write("HP: " + str(hp) + "\n")
        archivo.write("Fuerza: " + str(fuerza) + "\n")
        archivo.write("Inteligencia: " + str(inteligencia) + "\n")
        archivo.write("Agilidad: " + str(agilidad) + "\n")
        archivo.write("--------------------\n")
        
#y aqui ya cierra el archivo

        archivo.close()
        
#esto solo muestra el mensaje de creado y un texto en blanco

        print("Personaje guardado correctamente.")
        print("")
        
#ahora vamos con lo que pasa en la opcion 2

    elif opcion == "2":
        
#aqui abre el archivo en modo leer ("r"),
#guarda el archivo.read en la variable "contenido",
#y lo cierra

        archivo = open("personajes_dnd.txt", "r")

        contenido = archivo.read()

        archivo.close()

#muestra un espacio en blanco, el texto de personajes guardados
#y muestra lo que hay en la variable contenido


        print("")
        print("--- PERSONAJES GUARDADOS ---")
        print(contenido)

#por último, la opción 3

    elif opcion == "3":

        print("¡Hasta la próxima, aventurero!")

#esto es lo que muestra si no se eligío 1,2 o 3 en el menú principal
#(lo de crear personaje, ver personajes y salir
    else:

        print("")
        print("Opción no válida.")
        print("Elige una opción del 1 al 3.")
        print("")
        
#y este es el fin del código :)