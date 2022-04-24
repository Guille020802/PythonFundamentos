


def ingreso_entero(msg :str ="Ingrese un número entero: ") -> int:
    """Retorna un número entero solicitado al usuario"""
    try:
        x = int(input(msg))
        return x
    except:
        #print('Ingrese bien el numero')
        return ingreso_entero(msg)
    
def main():
    
    x = ingreso_entero("Ingrese el primero número entero: ")
    y = ingreso_entero("Ingrese el segundo número entero: ")
    
    if y == 0:
        print('División entre 0 no posible')
    else:
        division = x / y
        print(f'El resultado es {division}')
    pass


# 
try:
    main()
except Exception as e:
    print(e)
finally:
    print('Finalizando el programa')