
# ESCRIBIR UN PROGRAMA MENU QUE REALICE LAS SIGUIENTES TAREAS:
# 1. REALIZAR LA SUMA DE  2 NROS
# 2. CALCULAR EL FACTORIAL DE UN NRO
# 3. MOSTRAR UN TRIANGULO DE ALTURA 'H' POBLADO DE '#'
# 4. CALCULAR EL AREA DE UN CIRCULO
# 5. SALIR DEL CODIGO
# ADICIONALES: 
# - DEBEMOS IMPLEMENTAR VALIDACIONES AL INGRESO DE DATOS
# - UTILIZAR FUNCIONES


# 1. librerias 
import math

# import validacion_datos
import validacion_datos as v # importando con alias

# 2. CONSTANTES 
MSG = """¿Qué quieres hacer? Escribe una opción
    1) Sumar dos números
    2) Calcular factorial de un números
    3) Mostrar un triangulo de altura 'h'
    4) Calcular el área de un circulo
    5) Salir
    Opcion: """

# 3. funciones y/o clases

def calcular_factorial_recursivo(x: int):
    """ Retorna el factorial de un nro 'x' en forma recursiva
    """
    if x in [1, 0]:
        return 1
    elif x>1:
        return x * calcular_factorial_recursivo(x-1)

def sumar(x:float, y:float):
    return x + y

def mostrar_triangulo(h:int):
    for i in range(h):
        print(  '#' * (i+1))
    
def calcular_area_circulo(r:int, pi:float=3.14):
    area  = pi * math.pow(r,2)
    return area 

# 4. mi programa principal

print("Bienvenido al menú interactivo")
while True:
    opcion = input(MSG)
    if opcion == '1':
        n1 = v.ingrese_numero_float("Introduce el primer número: ")
        n2 = v.ingrese_numero_float("Introduce el segundo número: ")
        suma = sumar(n1, n2)
        print(f"El resultado de la suma es: {suma}")
    elif opcion == '2':
        numero = v.ingrese_numero_entero('Ingrese un nro para el calculo del factorial: ')
        factorial = calcular_factorial_recursivo(numero)
        print("El factorial de {x}! es {y}".format(x=numero, y=factorial))
    elif opcion =='3':
        altura = v.ingrese_numero_entero('Ingrese la altura del triangulo: ')
        mostrar_triangulo(altura)
    elif opcion =='4':
        radio = v.ingrese_numero_float("Introduce el radio: ")
        area_circulo = calcular_area_circulo(radio)
        print('El area del circulo es {area}'.format(area=area_circulo))
    elif opcion =='5':
        print("¡Hasta luego! Ha sido un placer ayudarte")
        break
    else:
        print("Comando desconocido, vuelve a intentarlo")