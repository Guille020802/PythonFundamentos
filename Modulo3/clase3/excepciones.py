# Solcita el ingreso de un número entero positivo 'n'.
#  E imprimir un triángulo de altura n

def validar_ingreso_numero(msg= 'Ingrese un número entero: '):
    """Realiza las validaciones para el ingreso de un número"""
    try:
        n = int(input(msg))

        if n>1:
            return n
        
        print('Ingrese un número entero positivo ....')
        return validar_ingreso_numero(msg)
    except:
        print('No es un número, vuelva a intentar....')
        return validar_ingreso_numero(msg)


# 1. Ingreso de datos
n = validar_ingreso_numero()
print(n)


# 2. Muestro triángulo
for i in range(1,n+1):
    print('*'*i)



# 1. Ingreso de datos
# while True:
#     try:
#         # solicita número
#         n = int(input('Ingrese un entero: '))

#         if n>=1:
#             break
#         print('Ingrese un número entero positivo ....')
#     except:
#         print('No es un número')
#     pass
# # 2. Muestro triángulo
# for i in range(1,n+1):
#     print('*'*i)


