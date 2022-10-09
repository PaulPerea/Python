print("##################################################")
print("+ Programa para deterinar ¿Cuál es el número más gande de los tres números? +")
print("##################################################")

num1 = int(input("Introduce el primer número: "))
num2 = int(input("Introduce el segundo número: "))
num3 = int(input("Introduce el tercer número: "))

if num1 > num2 and num1 > num3:
    print(num1)
elif num2 > num3:
    print(num2)
else:
    print(num3)
