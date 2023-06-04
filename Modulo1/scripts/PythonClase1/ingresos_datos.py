"""
Imagina que acabas de abrir una nueva cuenta de ahorros que te ofrece el 4% de interés al año. 
Estos ahorros debido a intereses, que no se cobran hasta finales de año, se te añaden al balance final 
de tu cuenta de ahorros. 

Escribir un programa que comience leyendo la cantidad de dinero depositada en la cuenta de ahorros, 
introducida por el usuario. Después el programa debe calcular y mostrar por pantalla la cantidad de 
ahorros tras el primer, segundo y tercer años. Redondear cada cantidad a dos decimales.
"""

INTERES = 0.04

# 1. Solicito saldo contable en cuenta
saldo_contable = float(input('Ingrese la cantidad de dinero en su cuenta: ')) # input retorna un str


# Calculo los balances en cuenta contable para el 1,2,3 año
# monto_final = saldo_contable * (1+INTERES)**t

monto_final = saldo_contable * (1+INTERES) #-> 1er año
monto_final_2 = monto_final * (1+INTERES)
monto_final_3 = monto_final_2 * (1+INTERES)

# muestro en pantalla los resultados
print(f'INTERES: {INTERES:.0%}\n CAPITAL: {saldo_contable}\n MONTO FINAL 1ER AÑO:{monto_final}')
print(f'El balance al final del 2er año será {monto_final_2}')
print(f'El balance al final del 3er año será {monto_final_3}')



