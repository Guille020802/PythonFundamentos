


def ingrese_float(msg:str= 'Ingrese un número flotante: ')->float:
    """Solicitar el ingreso de un número"""
    try:
        return float(input(msg))
    except:
        return ingrese_float(msg)
    
def calcular_discriminante(a:float,b:float,c:float)-> float:
    """Calcula el discriminante de una función cuadrática

    Args:
        a (float): ax2
        b (float): bx
        c (float): c

    Returns:
        float: Retorna discriminante de la función cuadrática
    """
    
    return (b**2)-4*a*c
    
# # pruebo la funcion
# x = ingrese_float()
# print(x)