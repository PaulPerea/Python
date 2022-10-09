import random

def adivina_num_com(x):
    print("===========================")
    print("¡Bienvenido al Juego!")
    print("===========================")
    print(f"Selecciona un número entre 1 al {x} para que la computadora adivine")

    lim_inf = 1
    lim_sup = x
    res = ""

    while res != "c" :
        #Genera predicion
        if lim_inf != lim_sup:
            predicion = random.randint(lim_inf,lim_sup)
        else:
            predicion = lim_inf

        #Obtener rpt del usuario
        res = input(f"Mi respuesta es {predicion}. Si es muy alta ingresa (A). Si es muy baja ingresa (B). Si es correcta ingresa (C) : ").lower()
            

        if res == "a":
            lim_sup = predicion - 1
        elif res == "b":
            lim_inf = predicion + 1

    print(f"Si , la computadora ah adivinado el número en que esta pensando")
adivina_num_com(10)
