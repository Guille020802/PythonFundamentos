



# genero plantilla
class Persona:
    # atributos
    
    # clase inicializado
    def __init__(self, nombre, apellido, anio_nacimiento):
        """Solicita atributos de la persona """
        self.nombre = nombre 
        self.apellido = apellido
        self.born_year = anio_nacimiento
        pass
    
    # metodos
    def comer(self):
        print('Comiendo ...')
        
    def caminar(self):
        print('Caminar ...')
        
    def calcular_edad(self, anio_actual):
        """Calculo la edad de una persona"""
        edad = anio_actual - self.born_year
        print( 'La persona posee {} años'.format(edad) )
        

# Necesito generar un objeto a partir de mi plantilla(clase)
persona1 = Persona('Gonzalo', 'Delgado', 1994)

persona2 = Persona('Luis', 'Miranda', 2000)

# obteniendo datos de mi objeto
print('----- Persona1 --------')
datos_persona = "nombre: {}\napellido: {}".format( persona1.nombre, persona1.apellido  )
print(datos_persona)

print('----- Persona2 --------')
datos_persona = "nombre: {}\napellido: {}".format( persona2.nombre, persona2.apellido  )
print(datos_persona)


    
        
        


