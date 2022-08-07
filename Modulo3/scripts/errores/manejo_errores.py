# https://www.programiz.com/python-programming/exception-handling

try:
    #intento ejecutar el bloque de código
    n = float(input("Introduce un número: "))
    m = 4
    print("{}/{} = {}".format(m, n,m/n))

except ZeroDivisionError: # un error en específico
    print('División entre 0, revise su dato de entrada')    

except Exception as e: # para todos los errores en general 'Exception'
    # en caso algo falle, ejecuto una excepción
    print(e)
    print("Ha ocurrido un error, introduce bien el número")