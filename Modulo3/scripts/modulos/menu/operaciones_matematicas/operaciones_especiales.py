def calcular_factorial(n):
    factorial = 1
    for i in range(2,n+1):
        factorial = i * factorial
    return factorial

def es_primo(numero:int):
    """
    Evaluar si un numero dado es o no es primo

    Args:
        numero (int): Numero entero a evaluar

    Returns:
        bool: True en caso Primo, False en caso No Primo
    """
    primo = True
    for j in range(2,numero):
        # Si existe algún otro divisor entre (2 y n-1): Numero no primo
        if numero % j == 0:
            primo = False
            break
    return primo
