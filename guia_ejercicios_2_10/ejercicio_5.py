from math import sqrt

while True:
    num = int(input("Ingrese un numero: "))

    try:
        num = sqrt(num)
        break
    except:
        print("Ingrese un numero no negativo")
print(num)