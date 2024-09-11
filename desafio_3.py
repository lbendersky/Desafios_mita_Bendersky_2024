discos = [
    [101, "Frank", "amy Winehouse", "Soul"],  
    [102, "Back to Black", "amy Winehouse", "Soul"], #mismo nombre
    [101, "Another ticket", "eric Clapton", "Blues"], #id repetido || crei que era mucho adaptar el codigo para este caso improvable por lo que no lo hice
    [103, "Medias Negras", "memphis la blusera", "Blues"],
    [104, "Almendra", "almendra", "Rock"] 
]

def organizar(disco):
    discos_r = [[id, nombre[:6], artista[:7], genero[:6]] for id, nombre, artista, genero in disco]

    for i in range(len(discos_r)):
        discos_r[i][2] = discos_r[i][2].capitalize()

    discos_o = sorted(discos_r, key=lambda x: (-x[0], x[1]))

    return discos_o

def main():
    discos_o = organizar(discos)
    flag = 0
    ite = -1

    while flag == 0:

        if ite == 0:
            discos_o = organizar(act_disc)
            ite = -1

        accion = int(input("Seleccione una accion: 1-crear, 2-leer, 3-actualizar, 4-eliminar, 5-terminar: "))
        if accion == 1:
            act_disc = crear(discos_o)
            ite = 0
        elif accion == 2:
            leer(discos_o)
        elif accion == 3:
            act_disc = actualizar(discos_o)
            ite = 0
        elif accion == 4:
            act_disc = eliminar(discos_o)
            ite = 0
        else:
            flag = 1


def crear(act_org):
    discos.append([]) 

    for col in act_org[0]:
        act_org[len(act_org) - 1].append(0)
    
    nom = input("Ingrese nombre del album: ")
    art = input("Ingrese artista: ")
    gen = input("Ingrese genero: ")
    
    act_org[len(act_org) - 1][0] = act_org[len(act_org) - 2][0] + 1
    act_org[len(act_org) - 1][1] = nom
    act_org[len(act_org) - 1][2] = art
    act_org[len(act_org) - 1][3] = gen

    return act_org


def leer(org):
    print(f"{'Id' :>4}{'Nombre' :^10}{'Artista' :^10}{'Genero' :<4}")
    print("-" * 30)

    for id, nombre, artista, genero in org:
         print(f"{id :>4}{nombre :^10}{artista :^10}{genero :<4}")


def actualizar(act_org):
    nro_act = int(input("Ingrese que dato quiere actualizar: 1-id, 2-nombre del album, 3-artista, 4-genero: "))

    if nro_act == 1:
        pos = int(input("Ingrese el id que desea cambiar: "))

        band = 0
        x = -1
        while band == 0 and x < len(act_org) - 1:
            x += 1
            if act_org[x][0] == pos:
                band = 1
        
        if band == 1:
            act_org[x][0] = int(input("Ingrese el id por el que desea cambiarlo: "))
            return act_org
        else:
            print("No se encontro el id")
    else:
        pos = int(input("Ingrese el id de la fila que desea cambiar: "))

        band = 0
        x = -1
        while band == 0 and x < len(act_org) - 1:
            x += 1
            if act_org[x][0] == pos:
                band = 1
        if band == 0:
            print("No se encontro el id")
        else:
            opcion = int(input("Ingrese el numero perteneciente a la categoria que desea cambiar: 1-nombre, 2-artista, 3-genero "))

            if opcion == 1:
                act_org[x][1] = input("Ingrese el nombre del album por el que reemplazarlo: ")
                return act_org
            elif opcion == 2:
                act_org[x][2] = input("Ingrese el nombre del artista por el que reemplazarlo: ")
                return act_org
            elif opcion == 3:
                act_org[x][3] = input("Ingrese el nombre del genero por el que reemplazarlo: ")
                return act_org
            else:
                print("Numero incorrecto")


def eliminar(act_org):
    pos = int(input("Ingrese el id que desea cambiar: "))

    band = 0
    x = -1
    while band == 0 and x < len(act_org) - 1:
        x += 1
        if act_org[x][0] == pos:
            band = 1
    
    if band == 1:
        act_org.pop(x)
        return act_org
    else:
        print("No se encontro el id")


main()