

letra = input('Ingrese una letra: ')

#'l' -> longitud 1

if len(letra)==1:
    if letra in 'aeiou':
        print('es una volcal')
    else:
        print(f'Se ingreso la letra {letra}')
else:
    print('No se puede procesar el caso')
