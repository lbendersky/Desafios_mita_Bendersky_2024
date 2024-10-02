from random import randint

adivinar = randint(1, 500)
intentos = 0

while True:
    try:
        num = int(input("Ingrese un numero: "))
        intentos += 1

        if num < adivinar:
            print("el numero es mas grande")
        elif num > adivinar:
            print("el numero es mas chico")
        else:
            print(f"Te llevo {intentos} intentos")
            break
    except (ValueError):
        intentos += 1
        print("No es un numero valido")