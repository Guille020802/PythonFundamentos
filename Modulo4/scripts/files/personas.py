

# leemos archivo
data = open('./personas.txt', encoding='utf-8').readlines()

# persona = {
#     'indice': 1,
#     'nombre': nombre,
#     'apellido': appelido,
#     'fecha_nacimiento': fecha_nacimiento
# }

# Limpieza de datos
listado_personas = list()
for p in data:
    persona = dict()
    datos_persona = p.split(';')
    
    persona['indice'] = datos_persona[0]
    persona['nombre'] = datos_persona[1]
    persona['apellido'] = datos_persona[2]
    persona['fecha_nacimiento'] = datos_persona[3].strip()
    
    # append
    listado_personas.append(persona)
    
# Visualizando info
# print(listado_personas)

for p in listado_personas:
    
    print("="*20 + f" {p['indice']} " + "="*20)
    
    datos_print = """
    Nombre: {nombre}
    Apellido: {apellido}
    Fecha Nacimiento: {fecha_nacimiento}
    """ 
    print(datos_print.format(nombre=p['nombre'], apellido=p['apellido'],fecha_nacimiento=p['fecha_nacimiento']  ) )
