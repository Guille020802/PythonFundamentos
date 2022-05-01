
# https://realpython.com/python-datetime/
import time

from datetime import datetime, timedelta




fecha_actual = datetime.now() # 2022-05-01 11:43:25.429759


mi_fecha = datetime(2020, 12, 15)
anio = mi_fecha.year
mes = mi_fecha.month
dia = mi_fecha.day


print(mi_fecha)

print('Fecha con formato de usuario: '+ mi_fecha.strftime('%d/%m/%Y'))



print( anio)



print(fecha_actual)
nueva_fecha = fecha_actual + timedelta(days=5)

print(nueva_fecha)


print('Parando el programa unos segundos')
time.sleep(5)

print('Finalizamos')

# print(fecha_actual)










