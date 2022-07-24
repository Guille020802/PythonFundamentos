

# Imprimir todos los numeros primos entre 1 y 100 -> Quiero evaluar 100 numeros

for num in range(1,101):
    # evaluo cada numero
    
    # divisores
    primo = True
    for i in range(2, num):
        # evaluo si existe un divisor
        if num % i == 0:
            primo=False
            break
        
    if primo:
        print(num)
        



# # EVALUABA 1 CASO -> saber si un numero introducido es primo o no

# # un numero no es primo, si existe un divisdor diferente a 1 y 'n'
# num = int(input('Escriba un numero entero: '))



# if primo:
#     print('El numero es primo')
# else:
#     print('El numero no es primo')
    



