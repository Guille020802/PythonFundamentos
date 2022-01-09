
# defino mi clase auto
class Auto:
    def __init__(self, marca, modelo, color, nro_placa, costo):
        # variables de mi auto
        self.marca = marca
        self.modelo = modelo
        self.color = color
        self.nroPlaca = nro_placa
        self.precio_compra = costo
    
    # Métodos o Funciones
    def acelerar(self):
        print('Acelerando mi auto ..')
    
    def frenar(self):
        print('Frenando mi auto')
        
    def caracteristicas_auto(self):
        print('Tengo un auto de marca: {} y modelo: {}'.format(self.marca, self.modelo ))
        
    def calcular_precio(self, years):
        # simulando depreciacion del 10% por año de uso
        return self.precio_compra * ((1 -0.1) ** years)
    
if __name__ == '__main__':
    
    # Creo mi objeto Auto
    auto1 = Auto('Toyota', 'Jaguar', 'rojo','APX789', 10000)
    auto2 = Auto(color='plomo',
                 marca ='Kia',
                 modelo='Picanto',
                 nro_placa='AYT562',
                 costo=5000)
    
    # auto3 = Auto('Toyota', 'Jaguar', 'rojo','APX789', 10000)
    # print(auto1 == auto3)
    
    # Imprimiendo valores auto1
    print('----------AUTO1 ------------')
    # OBTENIENDO CARACTERISTICAS DE MI OBJETO
    print( 'Placa : ', auto1.nroPlaca  )
    print('COLOR : ', auto1.color )
    
    # EJECUTANDO LOS METODOS DE MI AUTO1
    auto1.acelerar()
    
    precio_actual = auto1.calcular_precio(5)
    print(f'La el valor actual del vehiculo es {precio_actual}')
    
    
    print('----------AUTO2 ------------')
    # OBTENIENDO CARACTERISTICAS DE MI OBJETO
    print( 'Placa : ', auto2.nroPlaca  )
    print('COLOR : ', auto2.color )
    
    auto2.caracteristicas_auto()
    
    
    
    
    
    
    
    