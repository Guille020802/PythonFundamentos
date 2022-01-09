# librerias


# constantes


# Funciones y/o Clases

def ingreso_entero(msg :str = 'Ingrese un número entero: '):
    try:
        numero = int(input(msg))
        return numero
    except:
        print('Error! Vuelva a intentar')
        return ingreso_entero(msg)
    
def ingreso_float(msg :str = 'Ingrese un número decimal: '):
    try:
        numero = float(input(msg))
        return numero
    except:
        print('Error! Vuelva a intentar')
        return ingreso_entero(msg)
    

# 4. Mi programa
if __name__ == '__main__':
    numero_entero = ingreso_entero()
    numero_decimal = ingreso_float()
    
    print(numero_entero)
    print(numero_decimal)

