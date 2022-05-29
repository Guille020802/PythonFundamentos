import math


# Las funciones, me ayudan a separar lógicas de mi código
# a manera de empaquetar dichas lógicas y que mi código se vea lo más limpio posible

def es_divisible(numero, i):
    """Evalua si el número es divisible por un número 'i' o no. Devuelve True o False"""
    return (numero % i == 0)


def es_primo(n: int)->bool:
    """Retorna True si el número ingresado es primo, en otro caso retorna False
    """
    primo = True
    x = int(math.sqrt(n)) + 1
    
    for i in range(2,x):
        if es_divisible(n, i):
            primo=False # demuestras que no es primo
            break
    
    return primo
    

# pido dato
numero = int(input("ingrese el numero: "))

# muestro en pantalla
if es_primo(numero):
    print("Es primo")
else:
    print("No es primo")


# las funciones me permiten reutilizar las l+ogica cuando sean requeridas

if es_primo(100):
    print("Es primo")
else:
    print("No es primo")


if es_primo(251):
    print("Es primo")
else:
    print("No es primo")
