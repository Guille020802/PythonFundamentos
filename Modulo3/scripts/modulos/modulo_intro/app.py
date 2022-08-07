# Algunos unas un archivo app.py como archivo principal, para el llamado de otros paquetes

# llamo a mi archivo que contiene la función que requiero
# import funcionalidades

# import <nombre_archivo> as 'alias_archivo'
import funcionalidades as libs # genero un alias para el modulo


ECUACION = '{a}x2 + {b}x + c'

# de mi módulo, llamo a la función que deseo utilizar
a = libs.ingrese_float('Ingrese un numero para "a" : ')
b = libs.ingrese_float('Ingrese un numero para "b" : ')
c = libs.ingrese_float('Ingrese un numero para "c" : ')


print(ECUACION.format(a=a, b=b, c=c))

Disc = libs.calcular_discriminante(a,b,c)
if a != 0 and Disc > 0:
    print('x_1 = ', (-b+(Disc**0.5))/(2*a))
    print('x_2 = ', (-b-(Disc**0.5))/(2*a))
elif a !=0 and Disc == 0:
    print('x = :', (-b)/(2*a))
else:
    print('No tiene solucion real')

