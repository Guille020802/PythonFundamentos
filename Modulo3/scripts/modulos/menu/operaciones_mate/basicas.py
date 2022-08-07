def sumar(a,b):
    return a + b

def restar(a,b):
    return a -b

def multiplicar(a,b):
    return a * b

def dividir(a,b):
    try:
        return a / b
    except ZeroDivisionError:
        print('División 0')
        return 1
    
# validaciones
if __name__ == '__main__':
    
    print(sumar(5,9), 14)    # comparacion
    print(dividir(1,2) == 0.5)
    assert dividir(1,0)== 1   # compara
    # assert dividir(1,0)== 2 