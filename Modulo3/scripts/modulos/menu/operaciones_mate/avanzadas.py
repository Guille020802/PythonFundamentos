

def calcular_factorial_recursivo(numero:int)->int:
    """Calcula el factorial de un número de forma recursiva"""
    
    assert numero >0 # validamos numero mayor 1
    if numero == 1:
        return 1
    return numero * calcular_factorial_recursivo(numero -1)


def es_primo(numero:int)-> bool:
    """Evalua si un número dado es primo o no"""
    primo = True
    for i in range(2, numero):
        # evaluo si existe un divisor
        if numero % i == 0:
            primo=False
            break
    
    # retorna una respuesta
    return primo

if __name__ == '__main__':
    
    # validamos factorial
    assert calcular_factorial_recursivo(5) == 120
    
    assert es_primo(5) ==True
    
    