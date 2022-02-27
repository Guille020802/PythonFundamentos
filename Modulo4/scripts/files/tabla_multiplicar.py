import os

# n
n = int(input('Ingrese un nro del 1 al 10'))

# tabla de multiplicar para  n
tabla = [ f'{n} x {i} = {n * i}\n'  for i in range(1,13) ]

# escribiendo en archivo
ruta = f'./tabla-{n}.txt'
open(ruta, mode='w').writelines(tabla)
