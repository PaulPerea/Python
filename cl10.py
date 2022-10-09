print("Sistem para calcular el promedio de un alumno.")
nombre = input("Para comenzar, ¿Cuál es tu nombre?: ")
matematica = int(input(nombre + " ¿Cuál es tu calificación en matemáticas?: "))
quimica = int(input(nombre + " ¿Cuál es tu calificación en química?: "))
biologia = int(input(nombre + " ¿Cuál es tu calificación en biología?: "))
promedio = (matematica + quimica + biologia) / 3

if promedio >= 6:
    print('Felicidades ' + nombre + ' "aprobaste" con un promedio de: ', promedio)

print("Fin.")

