# 1. librerias


# 2. constantes

# 3. Funciones y/o Clases


# 4. mi Programa

try:
   n = int(input('Ingrese un número entero: ')) 
except:
    print('tomando un valor por defecto n=1')
    n=1


# calculo del factorial
factorial = 1
for i in range(2,n+1):
    factorial = i * factorial

print(f'el factorial de {n}! es {factorial}')









