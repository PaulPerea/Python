import random


def adivina_num(x):
    print("**************************")
    print("¡Bienvenido(a) al Juego!")
    print("**************************")
    print("Tu meta es adivinar el número generado por la computadora")

    num_ale = random.randint(1,x) #Número aleatorio entre 1 - x

    prediccion = 0

    while prediccion != num_ale:
        #El usuario ingres número
        prediccion = int(input(f"Adivina un número entre 1 y {x} :"))
        if prediccion < num_ale:
            print("Intenta otra vez. Este número es pequeño")
        elif prediccion > num_ale:
            print("Intenta otra vez. Este número es grande")
    print(f"¡Felicidades adivinaste el número {num_ale} correctamente.!")

adivina_num(10)
    
