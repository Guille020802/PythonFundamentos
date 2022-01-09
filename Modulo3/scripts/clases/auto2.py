# Librerias

# Constantes

# Funciones y/o clases   

class Auto:
    # atributos
    def __init__(self, nro_placa, tipo, color, modelo, anio_fabricacion):
        # genero las variables de auto
        self.nro_placa = nro_placa
        self.tipo = tipo
        self.color = color
        self.modelo = modelo
        self.anio_fabricacion = anio_fabricacion
    
    # establecemos funcionalidades 
    def print_fabricacion(self):
        print("El año de fabricacion del auto es {}".format(self.anio_fabricacion))

    def encender_auto(self):
        print("El auto se enciendo ....")

    def calcular_anios_uso(self, anio_actual):
        return anio_actual - self.anio_fabricacion
        
# Mi programa

# Generamos objetos
auto1 = Auto("AZ900", "deportivo", "amarillo","Toyota Yaris", 2019)
auto1.print_fabricacion()
auto1.encender_auto()
uso = auto1.calcular_anios_uso(2021)


# creamos un objeto 2
auto2 = Auto("EB856", "deportivo", "rojo", "Kia picanto", 2021)
auto2.print_fabricacion()
auto2.encender_auto()

print(uso)

print(auto1)

