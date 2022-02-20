# 1. Librerias


# Constantes

# 3. Funciones y/o clases

def ingrese_numero_entero(msg:str ="Ingrese un número entero: " ) -> int:
    """
    Valida el ingreso un numero entero
    
    Return : int
    """
    try:
        numero = int(input(msg))
        return numero
    except:
        print('Valida el ingrese del número, vuelvelo a intentar!')
        return ingrese_numero_entero(msg)
    
    
def ingrese_numero_float(msg:str ="Ingrese un número decimal: " ) -> float:
    """
    Valida el ingreso un numero entero
    
    Return : int
    """
    try:
        numero = float(input(msg))
        return numero
    except:
        print('Valida el ingrese del número, vuelvelo a intentar!')
        return ingrese_numero_float(msg)

# 4. Mi codigo




