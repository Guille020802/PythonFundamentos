"""Deseo generar un archivo excel para cada uno de los estados contenidos en la tabla partidos"""

import pandas as pd
import sqlite3

# 1. Lectura de db
with sqlite3.connect('./src/base_datos.db') as conn:
    query = 'select * from partidos'
    df = pd.read_sql_query(query, conn)

# Generar excel para Alabama

listado_estados = df.state.unique()

for nombre_estado in listado_estados:
    condicion = (df['state'] == nombre_estado)
    df_process = df[condicion]
    df_process.to_excel(f'./out/{nombre_estado}.xlsx', index=False, sheet_name=f'Reporte-{nombre_estado}')

