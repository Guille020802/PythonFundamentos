semaforo = input('Ingrese el estado del semaforo: ')
semaforo = semaforo.lower()

if semaforo == 'verde':
    print('Puede cruzar la calle')
elif semaforo == 'amarillo' or semaforo == 'rojo':
    print('No puede cruzar')
else:
    # ingresa cualquier otra cosa diferente a 'rojo', 'amarillo', 'verde'
    print('dato invalido')

print('Fin del programa!')

