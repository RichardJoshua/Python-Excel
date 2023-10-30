# pip install pandas
# pip install xlrd

import pandas as pd

archivo_excel = pd.read_excel('./Registros.xlsx')
print(archivo_excel.columns)

values = archivo_excel['index'].values  #Columna a tener en cuenta como ID o Index
print(values)

# columnas = ['Identificador', 'Nombre', 'Apellidos']
columnas = ['nada','index','id','nombre','col1','col2','fecha']
df_seleccionados = archivo_excel[columnas]

print(df_seleccionados)