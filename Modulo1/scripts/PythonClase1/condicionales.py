"""
1.
Crear un programa que permita decidir a una persona cruzar la calle o no según:

Si semáforo esta en verde cruzar la calle
Si semáforo esta en rojo o amarillo no cruzar
La persona debe poder ingresar el estado del semáforo por teclado
"""

# 1. Requiero conocer el estado del semaforo
# 2. Si el semaforo esta en verde, colocar cruzar la calle; 
# si el semaforo se encuentra en rojo o amarillo, no cruzar la calle
# cualquier otro caso, dar un mensaje de error

estado_semaforo = input('Ingrese el estado del semáforo: ')
estado_semaforo = estado_semaforo.lower().strip()

if estado_semaforo == 'verde':
    print('Puede cruzar')
elif estado_semaforo == 'rojo' or estado_semaforo =='amarillo':
    print('No cruzar la calle')
else:
    print('Dato invalido')
