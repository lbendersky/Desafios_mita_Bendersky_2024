frase = input("Ingrese algo: ")

conjunto = set(frase.split(" "))

print(conjunto)

conjunto = sorted(conjunto, key=len)

print(conjunto)