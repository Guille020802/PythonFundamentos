import sys


valores = sys.argv # listado de argumentos

n = int(valores[1])

with open(f'./tabla-{n}.txt', 'w') as f:
    for i in range(1, 13):
        texto=f'{i} x {n} = {i*n}\n'
        f.write(texto)
    
    


