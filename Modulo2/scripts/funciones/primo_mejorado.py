
# Escribir un programa que pida al usuario un número entero y muestre por pantalla si es un número primo o no.

# Definicion de nro primo -> Aquel nro que no tiene otros divisores más que el 1 y el mismo nro
# Un nro primo primo solo posee 2 divisores
# No es un Nro primo ->  Cantidad de divores del nro mayor a 2


def es_primo(numero):
    """Devuelve False si encuentra un divisor entre 2 y numero
        en otro caso True
    """
    
    primo = True
    for num in range(2, numero):
        # encontrando divisores
        if (numero % num == 0):
            primo = False
            break
    
    return primo
    

# 1. Ingreso Datos
msg = 'Ingrese un numero : '
numero = int(input(msg))

# 2. No es un Nro primo ->  Cantidad de divores del nro mayor a 2
if not es_primo(numero):
    print(f'El nro {numero} NO ES PRIMO')
else:
    print(f'El nro {numero} ES PRIMO')


