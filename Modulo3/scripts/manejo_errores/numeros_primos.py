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


# 4. Mi Programa

# Escribir un programa que permita obtener los numero primos entre 1 y n
# Donde n es un número introducido por teclado

# Criterio1: Un número primo es aquel que es divisible solo entre 1 y el mismo numero
# criterio2: El numero solo debe tener 2 divisores 1 y numero
# criterio3: Si el numero es divisible por algún otro numero entonces NO ES PRIMO

numero = ingreso_entero("Ingrese el numero a evaluar: ")

primo = True
for i in range(2,numero):
    # Si existe algún otro divisor entre (2 y n-1): Numero no primo
    if numero % i == 0:
        primo = False
        break
    
if primo:
    print(f'el numero es PRIMO')
else:
    print("el numero NO PRIMO")

