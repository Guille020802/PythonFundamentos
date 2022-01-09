import math

def sumar(a,b):
    """Retorna la suma de dos numeros

    Args:
        a (float): Numero 1
        b (float): Numero 2

    Returns:
        float: Suma de a + b
    """
    return a + b

def restar(a,b):
    return a - b

def multiplicar(a,b):
    return a * b

def dividir(a,b):
    if b == 0:
        print("Error, division por 0")
    else:
        return a / b

def potencia(a, n):
    """Retorna el valor de a elevado a la n
    """
    return math.pow(a,n)