string = input("Oración: ")
eli= input("ingrese eliminación")
substring = ""

indice = string.find(eli)
substring = string[0 : indice] + string[indice + len(eli) + 1 : ]

print(f"Cadena resultante {substring}")
