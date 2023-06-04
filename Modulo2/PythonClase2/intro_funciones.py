# Realiza un programa que me permita saber si un número es par o impar

# Importar librerias

# Importar funciones y/o clases


# Logica principal
def evaluar_par(n:int):
    """Evalua si un número ingresado es par o es impar"""
    return n % 2 == 0

# numero = 7

# if evaluar_par(numero):
#     print("El número es par")
# else:
#     print('El número es impar')

# Evaluar si un número de la lista es par o impar
# lista_numeros = [ 12,43,65,343,433,23]

# for numero in lista_numeros:
#     if evaluar_par(numero):
#         print('Existe al menos un numero par en el listado')
#         break  # Salir del bucle si encontramos un número par

#  Colocar en otra lista todos los numeros pares encontrados

lista_numeros = [ 12,43,65,343,433,23, 6,8]

lista_pares = list()
lista_impares = list()
for numero in lista_numeros:
    if evaluar_par(numero):
        lista_pares.append(numero)
    else:
        lista_impares.append(numero)
    
print(f'Lista pares {lista_pares}')
print(f'Lista Impares {lista_impares}')







