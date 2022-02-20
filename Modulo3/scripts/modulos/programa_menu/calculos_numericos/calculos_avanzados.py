import math



def calcular_factorial_recursivo(x: int):
    """ Retorna el factorial de un nro 'x' en forma recursiva
    """
    if x in [1, 0]:
        return 1
    elif x>1:
        return x * calcular_factorial_recursivo(x-1)
    
def calcular_area_circulo(r:int, pi:float=3.14):
    area  = pi * math.pow(r,2)
    return area 