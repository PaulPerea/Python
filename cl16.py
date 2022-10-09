print("Bienvenido al sistema de Vacaciones solicitadas \n")
nom = input("Introduce tu nombre: \n")
clave = int(input("Introduce tu clave: \n"))
year = int(input("Introduce años trabajados: \n"))

if clave == 1:
    if year == 1:
        print("Estimado", nom ,"le corresponde 6 días de vacaciones. \n")
    elif year >= 2 and year <= 6:
        print("Estimado", nom ,"le corresponde 14 días de vacaciones. \n")
    elif year >= 7:
        print("Estimado", nom ,"le corresponde 20 días de vacaciones. \n")
    else:
        print("Estimado", nom ,"no le corresponde derechos a vacaciones \n")
elif clave == 2:
    if year == 1:
        print("Estimado", nom ,"le corresponde 7 días de vacaciones. \n")
    elif year > 1 and year < 7:
        print("Estimado", nom ,"le corresponde 15 días de vacaciones. \n")
    elif year > 6:
        print("Estimado", nom ,"le corresponde 22 días de vacaciones. \n")
    else:
        print("Estimado", nom ,"no le corresponde derechos a vacaciones \n")
elif clave == 3:
    if year == 1:
        print("Estimado", nom ,"le corresponde 10 días de vacaciones. \n")
    elif year > 1 and year < 7:
        print("Estimado", nom ,"le corresponde 20 días de vacaciones. \n")
    elif year > 6:
        print("Estimado", nom ,"le corresponde 30 días de vacaciones. \n")
    else:
        print("Estimado", nom ,"no le corresponde derechos a vacaciones \n")
else:
    print("Clave no existente \n")

print("Fin.")
