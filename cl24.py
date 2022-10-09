#Ejemplo para break
print("While con la sentencia break \n")
contador=0
while contador  < 10:
    contador +=1

    if contador == 5:
        break

    print("Valor actual de la variable: ", contador)

print("FIN del programa , la sentencia break se ah ejecutado.")

#Ejemplo para continue
print("\nWhile con la sentencia Continue \n")
contador=0
while contador  < 10:
    contador +=1

    if contador == 5:
        continue
        print("ga")
    

    print("Valor actual de la variable: ", contador)

print("FIN del programa , la sentencia continue se ah ejecutado.")
