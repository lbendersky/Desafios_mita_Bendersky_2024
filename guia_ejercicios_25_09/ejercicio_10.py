def eliminarclaves(dicc, claves):
    ite = 0

    for clave in claves:
        if clave in dicc.keys():
            del dicc[clave]
            ite += 1
    
    return dicc, ite

diccionario = {"Color": "rojo", "cantidad": 23, "Estado": "disponible"}
claves = ["Color", "Estado"]

uno, dos = eliminarclaves(diccionario, claves)
print(uno)
print(dos)