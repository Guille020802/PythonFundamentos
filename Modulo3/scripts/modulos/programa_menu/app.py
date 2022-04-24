# 1. Librerias
import validacion_datos as v # 'v' es un alias para referirme al modulo 'validacion_datos'

# from "nombre_sub_carpeta" import "nombre_archivo" as 'alias'
from funciones_avanzadas import maths_functions as m 

# 2. Constantes


# 3. Funciones y/o clases

def sumar(x: int, y: int)->int :
    """ Retorna la suma de x + y"""
    return x + y

def main():
        
    print("Bienvenido al menú interactivo")

    while True:
        print("""¿Qué quieres hacer? Escribe una opción
        1) Sumar 2 numeros enteros
        2) Calcular el factorial de un numero
        3) Área de la circunferencia
        4) Mostrar un triangulo
        5) Evaluar si un numero es primo
        6) Salir""")
        
        opcion = input() # me devuelve un string ''
        if opcion == '1':
            
            numero1 = v.ingreso_entero("Ingrese el primero número entero: ")
            numero2 = v.ingreso_entero("Ingrese el segundo número entero: ")
            
            suma = sumar(numero1, numero2)
            print(f'La suma de los numeros es: {suma}')
            
        elif opcion == '2':
            # 1. solicito ingreso de dato
            n = v.ingreso_entero()
            # 2. calculo factorial
            factorial = m.calcular_factorial_recursivo(n)
            # 3. muestro en pantalla resultado
            print(f'El factorial de {n} es {factorial}')
            
        elif opcion == '3':
            pass
        elif opcion == '4':
            pass
        elif opcion == '5':
            pass
        elif opcion =='6':
            print("¡Hasta luego! Ha sido un placer ayudarte")
            break
        else:
            print("Comando desconocido, vuelve a intentarlo")
    pass

# 4. Principal
try:
    main()
finally:
    print('Programa Finalizado')