import string
abecedario = string.ascii_lowercase # ingles

# 1. Ingreso de dato
# letra = input('Ingrese una letra: ')
# letra = letra.lstrip() # remuevo espacios en blanco

# #'l' -> longitud 1
# if len(letra)==1:
#     if (letra.lower() in abecedario) and (letra.lower() not in 'aeiou'):
#         print(f'Se ingreso la letra {letra}')
#     elif letra.lower() in 'aeiou':
#         print('es una volcal')
#     else:
#         print('No se puede procesar el caso')
# else:
#     print('No se puede procesar el caso')


while True:
    letra = input('Ingrese una letra: ')
    letra = letra.lstrip()
    
    if len(letra)==1:
        break # finalizar el bucle
    else:
        print('Ingrese un caracter de longitud 1')

# Evaluo letra
# letra pertenece al abecerario pero no es una vocal
if (letra.lower() in abecedario) and (letra.lower() not in 'aeiou'):
    print(f'Se ingreso la letra {letra}')
elif letra.lower() in 'aeiou':
    # si letra es una vocal
    print('es una volcal')
else:
    # otro caracter
    print('No se puede procesar el caso')

    
    
    