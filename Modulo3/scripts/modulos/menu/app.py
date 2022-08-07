# 1. importamos librerias
import ingreso_datos as ing

# from nombre_carpeta import nombre_archivo as 'alias'
from operaciones_mate import basicas

# from <modulo>.<archivo> import <funcion1>, <funcion2>, ....
from operaciones_mate.avanzadas import calcular_factorial_recursivo, es_primo

# 2. definimos constantes

BIENVENIDA_MENU = 'Bienvenido al menú interactivo'

OPCIONES_MENU = """
¿Qué quieres hacer? Escribe una opción
    1) Sumar dos números
    2) Muestre un triangulo de altura 'h'
    3) Juegar, de que color es una naranja
    4) Calcula el factorial de un número
    5) Validar si número es primo
    6) Salir
"""

# 3. generamos funciones y/o clases

def opcion1():
    
    n1 = ing.solicita_float("Introduce el primer número: ")
    n2 = ing.solicita_float("Introduce el segundo número: ")
    suma = basicas.sumar(n1,n2)
    print(f"El resultado de la suma es: {suma}")

def opcion4():
    numero = ing.solicita_entero()
    factorial = calcular_factorial_recursivo(numero)
    print(f'{numero}! = {factorial}')

def opcion5():
    numero = ing.solicita_entero()
    
    if es_primo(numero):
        print('El número {} es primo'.format(numero))
    else:
        print('El número {} No es primo'.format(numero))
        
def main():
    
    print(BIENVENIDA_MENU)
    while True: 
        opcion = input(OPCIONES_MENU) # me devuelve un string ''
        if opcion == '1':
            opcion1()
        elif opcion == '2':
            pass
        elif opcion == '3':
            pass
        elif opcion == '4':
            opcion4()
        elif opcion == '5':
            opcion5()
        elif opcion =='6':
            print("¡Hasta luego! Ha sido un placer ayudarte")
            break # rompe el bucle (salimos del menu)
        else:
            print("Comando desconocido, vuelve a intentarlo")
        
    pass # termino de funcion

# 4. programa principal
if __name__ == '__main__':
    try:
        main()
    except Exception as e:
        print(e)



