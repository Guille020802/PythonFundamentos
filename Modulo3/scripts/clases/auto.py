

# clases == model (los cuales me permiten generar múltiples objetos)
# clases == vienen a ser conceptos que ideamos 
# clases se componen de "atributos" (contantes, variables) y "métodos" (funciones, funcionalidades) 

# class <NombreClase> -> estilo camelcase
from datetime import datetime

ANIO = datetime.now().year

class Auto:
    
    # contantes
    nro_puertas = 4
    
    # atributos inicializadores
    def __init__(self, nro_placa, marca, modelo, anio_fabricacion:int) -> None:
        """Atributos con los que inicializaremos nuestro auto"""
        self.nro_placa = nro_placa
        self.marca = marca 
        self.modelo = modelo
        self.anio_fabricacion = anio_fabricacion
        
        # self -> permite definir la pertenencia de un atributo o método a la clase
        pass
    
    # Métodos
    def encender_motor(self):
        print('Encendiento el motor ...')
        pass
    
    def anios_antiguedad(self, anio_actual):
        """ Retorna la cantidad de años de antiguedad del vehiculo """
        return anio_actual -  self.anio_fabricacion
    pass

# Inicializando un objeto
auto1 = Auto('afx789', 'Kia', 'Picanto', 2021) # genero un objeto auto1 proveniente de mi molde Auto
auto2 = Auto('yxz564', 'Kia', 'Rio', 2020)

print('======= Auto1 =====')
print( 'PLaca: ', auto1.nro_placa )
print( '#Puertas: ', auto1.nro_puertas )
print( 'Modelo: ', auto1.modelo )
print( 'Fabricacion', auto1.anio_fabricacion )
print( 'Antiguedad', auto1.anios_antiguedad(ANIO) )


print('======= Auto2 =====')
print( 'PLaca: ', auto2.nro_placa )
print( '#Puertas: ', auto2.nro_puertas )
print( 'Modelo: ', auto2.modelo )
