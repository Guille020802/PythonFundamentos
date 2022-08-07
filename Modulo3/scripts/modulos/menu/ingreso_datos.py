






def solicita_entero(msg:str='Ingrese un número entero: ')->int:
    """ Solcita el ingreso de un número entero"""
    try:
        return int(input(msg))
    except:
        return solicita_entero(msg)

def solicita_float(msg:str='Ingrse un número decimal: ')->float:
    """ Solcita el ingreso de un número flotante"""
    try:
        return float(input(msg))
    except:
        return solicita_float(msg)