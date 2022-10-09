#Primer alternativa
nombre = "Carlos"
edad = 22

print("Hola {} tiene {} años.".format(nombre,edad))

#Segunda alternativa aqui tienes que especificar donde va cada format
print("Hola {nombre} tiene {edad} años.".format(nombre="Jean",edad=22))

#Tercera alternativa aqui tiene que ver la posicion con numeros
print("Hola {1} tiene {0} años.".format(edad,nombre))
