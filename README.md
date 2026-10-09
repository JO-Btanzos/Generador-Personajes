Proyecto: Generador Automático de Personajes (Estilo Dungeons & Dragons)

Contexto:

En los juegos de rol clásicos como Dungeons & Dragons, crear un personaje nuevo toma mucho tiempo. Los jugadores deben lanzar dados para definir sus atributos base y luego hacer cálculos matemáticos para sumar puntos extra dependiendo de su clase.

Este proyecto automatiza todo ese proceso. Es una herramienta muy interesante y útil porque funciona como un asistente real para Jugadores y "Dungeon Masters". Agiliza el inicio de las partidas al hacer las matemáticas al instante, evita errores de cálculo al momento de sumar atributos, y guarda toda la información de forma estructurada. Al final, crea un archivo que sirve como una "hoja de personaje digital" permanente, permitiendo a los usuarios tener un catálogo de héroes listos para jugar en cualquier momento.

Algoritmo:

Mostrar el menú principal: El programa inicia y muestra tres opciones: 1) Crear nuevo personaje, 2) Ver personajes guardados, 3) Salir.


Opción 1 - Crear un personaje:

El programa le pide al usuario que escriba el nombre de su personaje.

Le pregunta qué clase quiere ser, mostrando un menú más sencillo: 1) Guerrero, 2) Mago, 3) Bárbaro, o 4) Bardo.

La computadora elige números al azar (del 1 al 20) para tres atributos principales: Fuerza, Inteligencia y Agilidad.

El programa evalúa qué clase se eligió para dar bonificaciones a los atributos y calcular los Puntos de Vida.


Si es un Bárbaro, le suma 5 puntos a la Fuerza y le da 30 Puntos de Vida.

Si es un Guerrero, le suma 3 a la Fuerza y le da 25 Puntos de Vida.

Si es un Bardo, le suma 3 a la Agilidad y le da 20 Puntos de Vida.

Si es un Mago, le suma 5 a la Inteligencia y le da 15 Puntos de Vida.


El programa muestra en la pantalla un resumen del personaje con sus puntos finales y su vida.

Finalmente, guarda este resumen en un archivo llamado "personajes_dnd.txt."


Opción 2 - Ver personajes guardados:

El programa abre el archivo "personajes_dnd.txt" en modo de lectura.

Imprime en la pantalla todo lo que está escrito ahí. Así el usuario puede ver su colección completa de aventureros.


Opción 3 - Salir:

El programa se despide del usuario y se rompe el ciclo, terminando su ejecución :).

--------------------------------------------



Para mejorar el generador de personajes, investigué por mi cuenta el módulo `random` de Python, específicamente la función `random.randint()`.

Esta función permite generar números enteros aleatorios dentro de un rango establecido. La utilicé para asignar valores iniciales de fuerza, inteligencia y agilidad entre 1 y 20, haciendo que cada personaje tenga estadísticas diferentes.

Fuente de referencia: 

Python Software Foundation. (s. f.). *random — Generar números pseudoaleatorios*. Documentación oficial de Python. https://docs.python.org/es/3/library/random.html

https://youtu.be/nLKjIKz6zSI?si=KsCRuQBWUSJQSC5j

