
# Escribir un programa que pida al usuario un número entero y muestre por pantalla si es un número primo o no.

# Definicion de nro primo -> Aquel nro que no tiene otros divisores más que el 1 y el mismo nro
# Un nro primo primo solo posee 2 divisores
# No es un Nro primo ->  Cantidad de divores del nro mayor a 2


def divisores(numero):
    """Calcula la cantidad de Divisores de un nro
    """
    cantidad_divisores= 0
    for num in range(1, numero + 1):
        # encontrando divisores
        if numero % num == 0:
            cantidad_divisores +=1
    
    return cantidad_divisores
    

# 1. Ingreso Datos
msg = 'Ingrese un numero : '
numero = int(input(msg))

# 2. No es un Nro primo ->  Cantidad de divores del nro mayor a 2
nro_divisores = divisores(numero)
if nro_divisores!=2:
    print(f'El nro {numero} NO ES PRIMO')
else:
    print(f'El nro {numero} ES PRIMO')


