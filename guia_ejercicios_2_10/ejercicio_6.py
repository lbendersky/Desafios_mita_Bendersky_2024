lista = []

num = 0
while num != -1:
    num = int(input("Ingrese un numero: "))
    
    if num != -1:
        lista.append(num)

error = 0

while True:
    pos = int(input("Ingrese un numero en la lista: "))

    try:
        print(lista.index(pos))
    except (ValueError):
        error += 1

        if error == 3:
            print("Terminacion")
            break