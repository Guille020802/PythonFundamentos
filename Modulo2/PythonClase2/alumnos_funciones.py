# 1. Importacion de librerias
from pprint import pprint


# 2. Funciones y/o clases

def generar_listado_alumnos(num_alumnos:int):
    """Devuelve un listado de alumnos"""

    listado_alumnos = list()
    for i in range(num_alumnos):
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
    return listado_alumnos


def agregar_prom_notas_alumno(listado_alumnos:list):

    listado_copy = listado_alumnos.copy()

    for alumno in listado_copy:
        # A mi diccionario le agrego la llave prom_notas
        alumno['prom_notas'] = sum(alumno['notas'])/ len(alumno['notas'])

    return listado_copy

# 3. Mi logica

cantidad_alumnos = int(input('Ingrese la cantidad de alumnos a registrar: '))
# Generar Listado alumnos
listado_alumnos = generar_listado_alumnos(cantidad_alumnos)

print('Imprimiendo listado alumnos registrados')

pprint(listado_alumnos)

# Agregar el promedio de las notas por alumno

lista_modificada_alumnos = agregar_prom_notas_alumno(listado_alumnos)

print('Imprimiendo listado modificado alumnos')
pprint(lista_modificada_alumnos)







