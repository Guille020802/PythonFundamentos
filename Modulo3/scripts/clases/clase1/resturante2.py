from datetime import datetime
import time



class Restaurante:
    def __init__(self,nombre,tipo):
        self.nombre = nombre
        self.tipo = tipo
        
    def describe_restaurant(self):
        print('{},{}'.format(self.nombre, self.tipo))
    
    def open_restaurant(self, hora ):
        # poliforfismo
        apertura = datetime.now().replace(hour=12, minute=0, second=0, microsecond=0)
        cierre = datetime.now().replace(hour=21, minute=0, second=0, microsecond=0)
        
        if hora > apertura.time() and hora < cierre.time():
            print('El restaurante esta abierto')
        else:
            print('El restaurante esta cerrado')
    

if __name__ == '__main__':
    
    # Genero Objeto
    
    dicx_resturantes = {
        'r1':{
            'nombre': 'Mcdonals' ,
            'tipo': 'fastfood'
        },
        'r2':{
            'nombre': 'Dominos' ,
            'tipo': 'pizza'
        },
        'r3':{
            'nombre': 'EL pollo' ,
            'tipo': 'polleria'
        }
    }
    
    # Generando listado de objetos
    restaurantes = list()
    for key, val in dicx_resturantes.items():
        print('Creadondo objeto {}'.format(key))
        
        restaurantes.append( Restaurante(**val) )
    
    # invoco al metodo
    for restaurante in restaurantes:
        restaurante.describe_restaurant()
    
    
    pass