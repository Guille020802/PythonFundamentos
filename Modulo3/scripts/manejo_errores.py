
# normalmente nos equivocamos al momento de escribir código


# errores sintaxis
print('hola')
      
      
# errrores de nombre
print('hola')



# errores semanticas -> se detectan al momento de ejecutar el código

#x = int(input('ingrese un numero: ')) #1,2,3,4 ... 'Como estan'


# Excepciones -> formas en que controlamos los errores en python

try:
    # intenta hacer algo
    x = int(input('ingrese un numero: '))
except:
    # si algo salio mal, realiza otra cosa
    x=2

# x = int(input('ingrese un numero: '))

try:
    d = 100/x
except ZeroDivisionError:
    d = 100

print(d)





try:
    x = int(input('ingrese un numero: '))
    d = 100/x
except ValueError:
    d=50
except ZeroDivisionError:
    d=100
except: # para cualquier error
    d = 1
    



print(d)






