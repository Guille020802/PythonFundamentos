# 1. Librerias
import funciones # import el script

# 2. COnstantes

# 3. Funciones y/o clases

# Mi app principal
def main():
    
    persona = input('Ingrese su nombre: ')
    
    # llamo a la funcion saludar del archivo 'funciones'
    funciones.saludar(persona)
    
    # llamo a la funcion despedirse del archivo 'funciones'
    funciones.despedirse()
    pass

# 4. Llamando programa
try:
    main()
except Exception as e:
    print(e)
finally:
    print('Programa finalizado')


