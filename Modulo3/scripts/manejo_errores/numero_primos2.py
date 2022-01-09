# 1. Librerias

# 2.Constantes

# 3. Funciones y/o Clases

def ingreso_entero(msg :str = 'Ingrese un número entero: '):
    try:
        numero = int(input(msg))
        return numero
    except:
        print('Error! Vuelva a intentar')
        return ingreso_entero(msg)


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
    
    

# 4. Mi Programa

# Escribir un programa que permita obtener los numero primos entre 1 y n
# Donde n es un número introducido por teclado

n = ingreso_entero("Ingrese el numero a evaluar: ")


# evaluar una lista del 1 al n y obteniendo los numeros primos entre ese rango
listado_primos = []
for i in range(1, n+1):
    # evalua si número es primo o no
    primo = es_primo(i)
    
    # Si primo, lo agrego a lista
    if primo:
        listado_primos.append(i)

# imprimir listado de primos
print(f'Numeros primos en el rango de 1 a {n}: {listado_primos}')

