

def calcular_factorial(n: int)->int:
    """Calcula el factorial de un número n"""
    factorial = 1
    for i in range(1, n+1):
        factorial *= i
    return factorial

def calcular_factorial_recursivo(n: int)->int:
    """Calcular el factorial de un número de forma recursiva"""
    if n==1:
        return 1
    elif n > 1:
        return n * calcular_factorial_recursivo(n-1)
    

# pruebo mis funciones
x = calcular_factorial(5)
print(x == 120) # 

y = calcular_factorial_recursivo(3)
print(y == 6) # 