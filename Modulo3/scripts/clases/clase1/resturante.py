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
    restaurante1 = Restaurante('Mcdonals', 'fastfood')
    restaurante1.describe_restaurant()
    restaurante1.open_restaurant(datetime.now().time())
    
    
    
    pass