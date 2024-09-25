from re import match

def mail_a_tupla(correo):
    if match(r"[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$", correo):
        lista_correo = correo.replace("@", ".")
        nuevo_correo = lista_correo.split(".")
        return tuple(nuevo_correo)
    else: 
        tupla = ()
        return tupla
    

respuesta = input("Ingrese una direccion de correo electronico: ")
resultado = mail_a_tupla(respuesta)
print(resultado)