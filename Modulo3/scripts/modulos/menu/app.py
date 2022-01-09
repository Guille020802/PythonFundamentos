# 1. Importar librerias

import ingreso_datos as ing # 'ing' es el alias del modulo
from operaciones_matematicas import operaciones as oper
import operaciones_matematicas.operaciones_especiales as opere

from triangulos import triangulos as t


# 2. COnstantes
OPCIONES_MENU = """¿Qué quieres hacer? Escribe una opción
    1) Sumar dos numeros
    2) Factorial de un número
    3) Evaluar primos en rango
    4) Realizar media Aritmetica
    5) Mostrar un triangulo en pantall
    6) Salir
    """

# 3. Funciones y/o clases
def listado_primos(numero):
    list_primos = []
    for i in range(1, numero+1):        
        # Si primo, lo agrego a lista
        if opere.es_primo(i):
            list_primos.append(i)
    return list_primos

def main():
    print("Bienvenido al menú interactivo")
    while True:
        opcion = input(OPCIONES_MENU) # me devuelve un string ''
        
        if opcion == '1':
            # Sumar dos numero
            n1 = ing.ingreso_float('Ingrese el primer numero a sumar: ')
            n2 = ing.ingreso_float('Ingrese el segundo numero a sumar: ')
            suma = oper.sumar(n1, n2)
            
            print('La suma de los números {a} + {b} es: {suma}'.format(a=n1, b=n2, suma=suma))
            break
        elif opcion == '2':
            # fACTORIAL DE UN NUMERO
            n = ing.ingreso_entero('Ingrese el numero para el calculo del factorial: ')
            factorial = opere.calcular_factorial(n)
            
            print(f'el factorial de {n}! es {factorial}')
            break
        elif opcion =='3':
            # Evaluar primos en rango
            numero = ing.ingreso_entero()
            lista_primos = listado_primos(numero)
            
            print(f'Numeros primos en el rango de 1 a {numero}: {lista_primos}')
            break
        elif opcion =='4':
            # Realizar media Aritmetica
            break
        elif opcion =='5':
            # Mostrar un triangulo en pantall
            h = ing.ingreso_entero()
            t.mostrar_triangulo(h)
            
        elif opcion =='6':
            # Salir del programa
            print('Adios')
            break
        else:
            print("Comando desconocido, vuelve a intentarlo")
        pass   


# 4. Mi programa
if __name__ == '__main__':
    try:
        main()
        print("finalizo el programa ...")
    except Exception as e:
        # imprime el mensaje de error
        print(e)
        