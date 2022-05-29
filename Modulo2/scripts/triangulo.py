# con funciones

def calcular_area_rectangulo(base: float, altura: float)->float:
    """Retornar el área de un triangulo

    Args:
        base (float): Base del triangulo
        altura (float): Altura del triangulo

    Returns:
        float: Area del triangulo
    """
    area = base*altura
    return area

b = 15
h = 10

cadena = 'hola a todos'

area = calcular_area_rectangulo(b, h)
print(f'El área del rectangulo es {area} ')

