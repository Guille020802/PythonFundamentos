


# La idea en las funciones, es construir bloques de código que me permitan simplificar logica


def es_primo(numero:int)-> bool:
    """Evalua si un número dado es primo o no"""
    primo = True
    for i in range(2, numero):
        # evaluo si existe un divisor
        if numero % i == 0:
            primo=False
            break
    
    # retorna una respuesta
    return primo


# 1. Escribir un programa que pida al usuario un número entero y muestre por pantalla si es un número primo o no.
# un numero no es primo, si existe un divisdor diferente a 1 y 'n'
num = int(input('Escriba un numero entero: '))

# divisores
if es_primo(num):
    print('El numero es primo')
else:
    print('El numero no es primo')
    

# 2. Imprimir todos los numeros primos entre 1 y 100 -> Quiero evaluar 100 numeros
for num in range(1,101):
    # evaluo cada numero
    
    # divisores
    if es_primo(num):
        print(num)
        
# 2. Coloque en una lista todos los numeros primos entre 1 y 100 

lista_primos = []

for num in range(1,101):
    # evaluo cada numero
    
    # divisores
    if es_primo(num):
        lista_primos.append(num)
        
print(lista_primos)
        