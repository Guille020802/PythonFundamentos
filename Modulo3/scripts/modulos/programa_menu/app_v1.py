
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

# 4. mi programa principal

print("Bienvenido al menú interactivo")
while True:
    opcion = input(MSG)
    if opcion == '1':
        n1 = float(input("Introduce el primer número: "))
        n2 = float(input("Introduce el segundo número: "))
        print(f"El resultado de la suma es: {n1+n2}")
    elif opcion == '2':
        # 1. Solicitar el nro para aplicar su factorial
        numero = int(input('Ingrese un nro: '))
        factorial = calcular_factorial_recursivo(numero)
        # 3. Mostrando resultado
        print("El factorial de {x}! es {y}".format(x=numero, y=factorial))
    elif opcion =='3':
        print("mostrar triangulo")
    elif opcion =='4':
        print("área del circulo")
    elif opcion =='5':
        print("¡Hasta luego! Ha sido un placer ayudarte")
        break
    else:
        print("Comando desconocido, vuelve a intentarlo")