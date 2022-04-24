# 1. Inportacion de librerias
import math

# 2. DECLARACION DE CONSTANTES
PI = 3.14

# 3. Declaracion de funciones
def ingreso_entero(msg :str ="Ingrese un número entero: ") -> int:
    """Retorna un número entero solicitado al usuario"""
    try:
        x = int(input(msg))
        return x
    except:
        print('Ingrese bien el numero')
        return ingreso_entero()

def main():
    # ingrese de dato
    x = ingreso_entero()
    
    # logica
    potencia = math.pow(x, 2) #x**2
    print(f'la Potencia de {x} al cuadrado es : {potencia}')
    pass

# 4. Mi programa
try:
    main()
except:
    print('Hubo un fallo en el codigo')


