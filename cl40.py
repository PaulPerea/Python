string = input("Introduce un String para invertirlo: ")
string_reserved = ""

for character in string :
    string_reserved = character + string_reserved

print(string_reserved)
