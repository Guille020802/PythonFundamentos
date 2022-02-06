

# 1. solicitar edad
edad = int(input('Ingrese su edad: '))

# validar si es mayor o menor de edad
if edad >= 18:
    msg = f'Persona de {edad} años! Es mayor de edad'
else:
    msg = f'Persona de {edad} años! Es menor de edad'


# dar respuesta
print(msg)