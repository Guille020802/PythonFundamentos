

# crear el molde 'clase'
class Auto: # los nombres de clase van en mayuscula y minuscula 'camelcase'
    
    # constantes
    nro_puertas = 4
    nro_ruedas = 4
    
    # definirle caracteristicas o propiedades o variables o constantes
    def __init__(self, nro_placa, marca, modelo, color) -> None:
        """Me permite ingresar datos obligatorios para la creacion del objeto"""
        self.placa = nro_placa
        self.marca = marca
        self.modelo = modelo
        self.color = color
        pass
    # PARA QUE SIRVE? definirle funcionalidades o comportamientos
    def encendido_motor(self):
        print('encender motor ...')
    
    def encender_radio(self):
        print('colocando estacion')
    
    def estado_gasolina(self, estado):
        self.estado_gas = estado
        print(f'El estado de la gasolina es {self.estado_gas}%')
        
    def cambio_placa(self, nueva_placa):
        self.placa = nueva_placa
        
    def imprimer_caracteristicas(self):
        print(f"""
              Placa: {self.placa}
              Modelo: {self.modelo}
              """)
    pass

# A partir de mi molde, creo mis objetos
auto1 = Auto('AZ800', 'Toyota', 'corola', 'azul')

# describiedo propiedades del auto
print('==========Auto1============')
auto1.imprimer_caracteristicas()

# funcionalidades
auto1.encendido_motor()
auto1.estado_gasolina(50)

auto1.cambio_placa('PE2000')
print(f'La placa del auto es {auto1.placa}')

# Auto2
auto2 = Auto('XP200', 'kia', 'rio', 'verde')

print('==========Auto2============')

auto2.imprimer_caracteristicas()