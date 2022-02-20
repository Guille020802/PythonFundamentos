
import math

# Funciones básicas matematicas
def sumar(x:float, y:float):
    return x + y

def restar(x:float, y:float):
    return x - y

def multiplicar(x:float, y:float):
    return x * y

def dividir(x:float, y:float):
    """Retorna x/y
    Returns:
        float: x/y
    """
    try:
        return x /y
    except ZeroDivisionError:
        print('Division entre 0')

def potencia(x:float, y:float):
    return math.pow(x, y)


# Testear
if __name__ == '__main__':
    print(sumar(1,2))
    print(dividir(8, 0))
