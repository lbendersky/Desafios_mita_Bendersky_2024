frase = input("Ingrese algo: ")

conjunto = set(frase.split(" "))

print(conjunto)

conjunto = list(conjunto)

flag = -1

while flag + 1 < len(conjunto) - 1:
    flag += 1
    if len(conjunto[flag]) < len(conjunto[flag + 1]):
        conjunto[flag], conjunto[flag + 1] = conjunto[flag + 1], conjunto[flag]
        flag = -1

print(conjunto)