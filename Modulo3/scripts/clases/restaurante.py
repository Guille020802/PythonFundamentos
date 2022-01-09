import datetime
import time

class Restaurant:
    def __init__(self,restaurant_name , cuisine_type):
        self.restaurant_name = restaurant_name
        self.cuisine_type = cuisine_type
    
    def describe_restaurant(self):
        print('Restaurant name: {}'.format(self.restaurant_name))
        print('Cuisine type: {}'.format(self.cuisine_type))
    
    def open_restaurant(self, hora_actual):

        if hora_actual > 12 and hora_actual<10:
            print("Restaurante abierto")
        else:
            print("Restaurante cerrado")

# Mi programa

# cree un objeto

datos_rest1={
    "restaurant_name": "Mcdonals",
    "cuisine_type": "fast food"
    }

datos_rest2={
    "restaurant_name": "Bembos",
    "cuisine_type": "fast food"
    }

datos_rest3={
    "restaurant_name": "Central",
    "cuisine_type": "Comida Gourmet"
    }

datos_restaurantes = [datos_rest1, datos_rest2, datos_rest3]

# restaurante1 = Restaurant(**datos_rest1)
# restaurante2 = Restaurant(**datos_rest2)
# restaurante3 = Restaurant(**datos_rest3)

# restaurante1.describe_restaurant()
# restaurante2.describe_restaurant()
# restaurante3.describe_restaurant()

# CREANDO OBJETOS RESTAURANTE
lista_restaurante_objetos = []
for data in datos_restaurantes:
    x = Restaurant(**data)
    lista_restaurante_objetos.append(x)


# IMPRIMEINDO VALORES RESTAURANTE
for i,restaurante in enumerate(lista_restaurante_objetos):
    print(f"-------------- RESTAURANTE {i+1} ---------------")
    restaurante.describe_restaurant()