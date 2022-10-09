print("#################################")
print("Calculadora de solo una variable")
print("#################################")

print("Panel de opciones ")
print("Presione 1 para suma ")
print("Presione 2 para restar ")
print("Presione 3 para Multiplicar ")
print("Presione 4 para Dividir ")

clav = int(input("Clave a elegir: \n"))

if clav == 1:
    nu=int(input("Primer valor: "))
    nd=int(input("Segundo valor: "))

    res = nu + nd
    print(res)
elif clav == 2:
    nu=int(input("Primer valor: "))
    nd=int(input("Segundo valor: "))

    res = nu - nd
    print(res)
    
elif clav == 3:
    nu=int(input("Primer valor: "))
    nd=int(input("Segundo valor: "))

    res = nu * nd
    print(res)
else:
    print("ya")
