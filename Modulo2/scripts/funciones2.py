
def sumar(a, b):
    return a + b

def restar(x,y):
    return x - y

def multiplicar(a,b):
    return a * b

def dividir(x,y):
    if y == 0:
        print("error")
    else:
        return x/y
    
    


print("Bienvenido al menú interactivo")
while True:
    print("""¿Qué quieres hacer? Escribe una opción
    1) sumar dos numeros
    2) restar dos numeros
    3) multiplicar dos numeros
    4) dividir dos numeros
    5) Salir""")
    
    opcion = input()
    if opcion == '1':
        n1 = float(input("Introduce el primer número: "))
        n2 = float(input("Introduce el segundo número: "))
        suma = sumar(n1, n2)
        print(f"El resultado de la suma es: {suma}")
        break
    elif opcion == '2':
        n1 = float(input("Introduce el primer número: "))
        n2 = float(input("Introduce el segundo número: "))
        resta = restar(n1, n2)
        print(f"El resultado de la resta es: {resta}")
        break
    elif opcion =='3':
        n1 = float(input("Introduce el primer número: "))
        n2 = float(input("Introduce el segundo número: "))
        multiplicacion = multiplicar(n1, n2)
        print(f"El resultado de la multiplicaciones es: {multiplicacion}")
        break
    elif opcion =='4':
        n1 = float(input("Introduce el primer número: "))
        n2 = float(input("Introduce el segundo número: "))
        dividir = dividir(n1, n2)
        print(f"El resultado de la division es: {dividir}")
        break
    elif opcion =='5':
        print(f"Adios!!")
        break
    else:
        print("Comando desconocido, vuelve a intentarlo")
    
    pass # end while

print("finalizo el programa")