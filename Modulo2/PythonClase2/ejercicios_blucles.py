# 1. Crear un listado de numeros ingresados por teclado. El cual contendra 5 .
# Calcular la suma de todos los numeros
# Calcular el promedio de los numeros
# Evaluar si alguno de los numeros es par.


listado_numeros = []  # Lista para almacenar los números ingresados

# Pedir al usuario que ingrese los números
for i in range(5):
    numero_solicitado = int(input("Ingrese un número: "))
    listado_numeros.append(numero_solicitado)  # Agregar el número a la lista

print("Números ingresados:", listado_numeros)


suma = sum(listado_numeros)  # Calcular la suma de los números
promedio = suma / len(listado_numeros)  # Calcular el promedio

print("Suma de los números:", suma)
print("Promedio de los números:", promedio)

# Verificar si alguno de los números es par
bool_par = False
for numero in listado_numeros:
    if numero % 2 == 0:
        bool_par = True
        break  # Salir del bucle si encontramos un número par

if bool_par:
    print("Al menos uno de los números es par")
else:
    print('Ninguno de los numeros en la lista es par')
