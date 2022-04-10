


# defino mi funcion la cual tiene 2 parametros
def sumar(a:int, b:int)->int:
    """Retorna la suma de a +b"""
    return a + b # return para devolver un valor o conjunto de valores

def get_int(msg='Ingrese un entero'):
    """Funcion que solicita al usuario un número entero

    Args:
        msg (str): El mensaje que tendra mi input. Defaults to 'Ingrese un entero'.

    Returns:
        int: Un número entero
    """
    return int(input(msg))

# 1. Solicito un entero
x = get_int('Ingrese x: ') # invoco a la funcion get_int
y = get_int('Ingrese y: ')
z = get_int() # usa el valor msg por defecto

# llamamos a la funcion sumar
sumar = sumar(x, y)

# Imprimo el valor de la suma
print(f'La suma de {x}, {y} es: {sumar}')