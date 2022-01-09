# 1. librerias


# 2. constantes

# 3. Funciones y/o Clases

def ingreso_entero(msg :str = 'Ingrese un número entero: '):
    try:
        numero = int(input(msg))
        return numero
    except:
        print('Error! Vuelva a intentar')
        return ingreso_entero(msg)

# 4. mi Programa

n = ingreso_entero()

# calculo del factorial
factorial = 1
for i in range(2,n+1):
    factorial = i * factorial

print(f'el factorial de {n}! es {factorial}')









