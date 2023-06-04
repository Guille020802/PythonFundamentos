# Se requiere imprimir la palabra "Hola" 10 veces
###################################################33


# print('Hola\n'*10)


# print('Hola')
# print('Hola')
# print('Hola')
# print('Hola')
# print('Hola')
# print('Hola')
# print('Hola')
# print('Hola')
# print('Hola')

# Bucle For y Bucle While

# for i in range(10):
#     print('Hola')



# Solcitar 10 numeros por teclado
########################################3

# numero_1 = int(input('Ingrese un número: '))
# numero_2 = int(input('Ingrese un número: '))
# numero_3 = int(input('Ingrese un número: '))
# numero_4 = int(input('Ingrese un número: '))
# numero_5 = int(input('Ingrese un número: '))
# numero_6 = int(input('Ingrese un número: '))
# numero_7 = int(input('Ingrese un número: '))
# numero_8 = int(input('Ingrese un número: '))
# numero_9 = int(input('Ingrese un número: '))
# numero_10 = int(input('Ingrese un número: '))

# 1. Creacion Lista Vacia
listado_numeros = list()

for i in range(1,11):
    #  Por cada usuario, solicito un numero y lo agrego a lista
    numero_ingresado = int(input(f'Ingrese un número {i}: '))
    listado_numeros.append(numero_ingresado)
    pass # no hace nada

# Imprimo el listado de números
print(listado_numeros)
print(i)
print(range(10))
print(*range(10))












