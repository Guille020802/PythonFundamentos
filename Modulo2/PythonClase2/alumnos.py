from pprint import pprint

# Se requiere realizar un sistema para un colegio, se le solcita almacenar los datos de n alumnos
# cuales contendran 3 Notas por cada alumno, Nombre, Edad

# Estructura a emplear
# alumno = {
#     'nombre' : 'Juan',
#     'edad': 20,
#     'notas': [12,12,12]
# }

# 
cantidad_alumnos = int(input('Ingrese la cantidad de alumnos a registrar: '))

listado_alumnos = list()
for i in range(cantidad_alumnos):
    print('='*10, i +1 , '='*10)
    nombre_alumno = input('Ingrese el nombre el alumno: ')
    edad_alumno = int(input('Ingrese la edad del alumno: '))

    # Solicito 3 notas 
    listado_notas = list()
    for j in range(3):
        nota = int(input(f'Ingrese la {j+1} nota: '))
        listado_notas.append(nota)

    # agrego diccionario a lista
    listado_alumnos.append({
        'nombre' : nombre_alumno,
        'edad' : edad_alumno,
        'notas' : listado_notas
        
    })

pprint(listado_alumnos)

# Agregar el promedio de las notas por alumno
for alumno in listado_alumnos:
    # A mi diccionario le agrego la llave prom_notas
    alumno['prom_notas'] = sum(alumno['notas'])/ len(alumno['notas'])
    pprint(alumno)

# Calcular el promedio general de notas. Sumar de promedios / cantidad de alumnos

sum_promedio = 0
for alumno in listado_alumnos:
    sum_promedio += alumno['prom_notas']
promedio_general = sum_promedio/ len(listado_alumnos)
print(f'El promedio general es de {promedio_general}')
































