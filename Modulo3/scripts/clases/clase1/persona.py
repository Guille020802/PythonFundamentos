



# genero plantilla
class Persona:
    # atributos estaticos
    nombre = 'Gonzalo'
    apellido= 'Delgado'
    anio_nacimiento = 1994
    
    # metodos
    
    def comer(self):
        print('Comiendo ...')
        
    def caminar(self):
        print('Caminar ...')
        
    def calcular_edad(self, anio_actual):
        """Calculo la edad de una persona"""
        edad = anio_actual - self.anio_nacimiento
        print( 'La persona posee {} años'.format(edad) )
        

# Necesito generar un objeto a partir de mi plantilla(clase)
persona1 = Persona()

# obteniendo datos de mi objeto
datos_persona = "nombre: {}\napellido: {}".format( persona1.nombre, persona1.apellido  )

print(datos_persona)
# de mi obtejo puedo utilizar sus metodos
persona1.calcular_edad(2022)



    
        
        


