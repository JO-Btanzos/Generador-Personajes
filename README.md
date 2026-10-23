Proyecto: Generador Automático de Personajes (Estilo Dungeons & Dragons)

----Contexto----

En los juegos de rol clásicos como Dungeons & Dragons, crear un personaje nuevo puede tomar tiempo. Los jugadores deben determinar sus atributos y realizar cálculos para aplicar bonificaciones dependiendo de la clase elegida.

Este proyecto busca automatizar parte de ese proceso mediante un programa que genera personajes, calcula sus estadísticas y organiza su información.

La herramienta está pensada como un asistente para jugadores y *Dungeon Masters*, ya que permite agilizar la creación de aventureros, reducir errores de cálculo y consultar los personajes generados durante la ejecución del programa.

El proyecto se desarrolla progresivamente conforme se aprenden y aplican nuevos conceptos de programación en Python.

----Algoritmo----

El programa muestra un menú principal con tres opciones:

1. Crear un nuevo personaje.
2. Ver los personajes guardados.
3. Salir.

---Opción 1: Crear un personaje---

El programa solicita al usuario el nombre de su personaje.

Posteriormente, permite elegir una raza entre las siguientes opciones:

1. Humano.
2. Elfo.
3. Enano.
4. Orco.

Después, solicita elegir una clase:

1. Guerrero.
2. Mago.
3. Bárbaro.
4. Bardo.

La computadora genera números aleatorios entre 1 y 20 para establecer tres atributos principales:

- Fuerza.
- Inteligencia.
- Agilidad.

A continuación, el programa aplica una bonificación según la clase seleccionada:

- **Bárbaro:** suma 5 puntos a la Fuerza y asigna 30 puntos de vida (HP).
- **Guerrero:** suma 3 puntos a la Fuerza y asigna 25 HP.
- **Bardo:** suma 3 puntos a la Agilidad y asigna 20 HP.
- **Mago:** suma 5 puntos a la Inteligencia y asigna 15 HP.

Después de aplicar las bonificaciones, ninguna estadística puede superar los 20 puntos.

El programa también solicita una descripción personalizada del personaje.

Finalmente, muestra un resumen con los datos del aventurero y almacena su información para poder consultarla desde la opción correspondiente.

---Opción 2: Ver personajes guardados---

El programa comprueba si existen personajes creados.

Si todavía no hay personajes, muestra un mensaje indicándolo.

Si existen personajes guardados, recorre la colección y muestra la información de cada uno, incluyendo su nombre, raza, clase, estadísticas, puntos de vida y descripción.

***Nota sobre el almacenamiento: actualmente, los personajes se guardan en un diccionario de Python durante la ejecución del programa. La escritura y lectura de un archivo llamado `personajes_dnd.txt` forman parte de la idea original, pero todavía deben implementarse en el código actual. Por ello, los personajes no permanecen guardados al cerrar el programa.

---Opción 3: Salir---

El programa muestra un mensaje de despedida y termina su ejecución.

----Información de cada personaje----

Cada personaje se representa mediante un diccionario que contiene los siguientes datos:

- Nombre.
- Raza.
- Clase.
- Fuerza.
- Inteligencia.
- Agilidad.
- Puntos de vida (HP).
- Descripción.

Los personajes se organizan en un diccionario principal que permite identificarlos mediante un número consecutivo.

---Características agregadas durante el desarrollo---

Además de las funciones contempladas en la idea original, se han incorporado las siguientes características:

- Sistema de razas:** permite elegir entre humano, elfo, enano y orco.
- Descripción personalizada:** permite escribir una descripción para cada personaje.
- Almacenamiento estructurado:** los datos de cada aventurero se organizan mediante diccionarios.
- Consulta de personajes:** permite visualizar los personajes creados durante la ejecución del programa.

Estas mejoras amplían las posibilidades de personalización y organización de los aventureros.

 Conceptos de programación utilizados

El proyecto aplica los siguientes conceptos de Python:

- Variables.
- Entrada de datos mediante `input()`.
- Salida de información mediante `print()`.
- Condicionales `if`, `elif` y `else`.
- Ciclos `while` y `for`.
- Funciones.
- Diccionarios.
- Cadenas de texto.
- Números enteros.
- Módulos y funciones de bibliotecas de Python.
- Generación de números aleatorios.

 ----Autoestudio----

Para mejorar el generador de personajes, se investigó por cuenta propia el módulo `random` de Python, específicamente la función `random.randint()`.

Esta función permite generar números enteros aleatorios dentro de un rango establecido. Se utiliza para asignar valores iniciales de Fuerza, Inteligencia y Agilidad entre 1 y 20, de modo que los personajes puedan tener estadísticas diferentes.

----Fuente de referencia----

Python Software Foundation. (s. f.). *random — Generar números pseudoaleatorios*. Documentación oficial de Python.

https://docs.python.org/es/3/library/random.html

También se consultó el siguiente recurso audiovisual:

https://youtu.be/nLKjIKz6zSI?si=KsCRuQBWUSJQSC5j

----Mejoras futuras----

Entre las posibles mejoras del proyecto se encuentran:

- Implementar el almacenamiento permanente de personajes en `personajes_dnd.txt`.
- Leer los personajes guardados en ese archivo al seleccionar la opción correspondiente.
- Incorporar armas e inventarios.
- Ampliar las opciones de personalización de los personajes.

Estas mejoras podrán desarrollarse conforme avance el proyecto y se incorporen nuevos conocimientos de programación.
