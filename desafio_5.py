from re import match

def veri_correo(correo):
    if match('^[a-zA-Z0-9._%+-]+@[azA-Z0-9.-]+\.[a-zAZ]{2,}$', correo):
        return 1
    else:
        return 0

def veri_telefono(telefono):
    if match('^\+?(\d{1,3})?\s?-?(\d{4})\s?-?(\d{4})\s?-?(\d{4})$', telefono):
        return 1
    else:
        return 0

def veri_postal(postal):
    if match('`^([A-Za-z]\d{4}[A-Zaz]{3})', postal):
        return 1
    else:
        return 0

def veri_fechas(fecha):
    if match('^\d{4}-\d{2}-\d{2}$', fecha):
        return 1
    else:
        return 0
