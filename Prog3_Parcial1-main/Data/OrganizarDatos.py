import pandas as pd


df = pd.read_csv('./Data/Arisaralda.csv')



df['fecha reporte web'] = pd.to_datetime(df['fecha reporte web'], format='%Y-%m-%d %H:%M:%S')
df['Fecha de notificación'] = pd.to_datetime(df['Fecha de notificación'], format='%Y-%m-%d %H:%M:%S')
df['Fecha de inicio de síntomas'] = pd.to_datetime(df['Fecha de inicio de síntomas'], format='%Y-%m-%d %H:%M:%S')
df['Fecha de muerte'] = pd.to_datetime(df['Fecha de muerte'], format='%Y-%m-%d %H:%M:%S')
df['Fecha de diagnóstico'] = pd.to_datetime(df['Fecha de diagnóstico'], format='%Y-%m-%d %H:%M:%S')
df['Fecha de recuperación'] = pd.to_datetime(df['Fecha de recuperación'], format='%Y-%m-%d %H:%M:%S')


df['Ubicación del caso'] = df['Ubicación del caso'].replace('casa', 'Casa')
df['Ubicación del caso'] = df['Ubicación del caso'].fillna('Casa')



df['Estado'] = df['Estado'].replace('leve','Leve')#normalización de dato leve
df['Estado'] = df['Estado'].fillna('Fallecido')#rellenar los nulos con Fallecido



df['Código ISO del país'] = df['Código ISO del país'].fillna(170)#los que no tienen codigo se infieren que son de colombia(ISO 170)



df['Nombre del país'] = df['Nombre del país'].fillna('COLOMBIA')#los que no tienen nombre del país se infieren que son de COLOMBIA



df['Recuperado'] = df['Recuperado'].replace('fallecido','Fallecido')#normalizar valores
df.loc[df['Edad'] >= 70, 'Recuperado'] = 'Fallecido'#en caso de ser de mas de 69 poner fallecido
df.loc[(df['Edad'] < 70) & (df['Edad']>=42 ), 'Recuperado'] = 'Activo'#en caso de estar entre 70 y 42 poner activo
df.loc[df['Edad'] < 42 , 'Recuperado'] = 'Recuperado'#en caso de ser menor a 42 poner recuperado


df['Fecha de inicio de síntomas'].fillna(df['fecha reporte web'], inplace=True)
#se pone en los registros de valor nan de fecha de inicio de síntomas el valor de la fecha de reporte web, siendo estos dos cercanos



df['Fecha de muerte'].fillna('2000-01-01 00:00:00', inplace=True)
#se infiere que si no tiene fecha de muerte es porque no murió por lo que se pone un dato atípico identificable que no se tenga en cuenta



df['Fecha de diagnóstico'].fillna(df['fecha reporte web'], inplace=True)
#se pone en los registros de valor nan de fecha de diagnóstico el valor de la fecha de reporte web, siendo estos dos cercanos



df['Fecha de recuperación'].fillna('2000-01-01 00:00:00', inplace=True)
#se infiere que si no tiene fecha de recuperación es porque murió por lo que se pone un dato atípico identificable que no se tenga en cuenta
df = df[df['Fecha de recuperación'] != df['Fecha de muerte']]




df['Tipo de recuperación'] = df['Tipo de recuperación'].replace('TIEMPO','Tiempo')#normalizar valores
df.loc[df['Recuperado'] == 'Fallecido', 'Tipo de recuperación'] = 'Fallecido'
df['Tipo de recuperación'].fillna('Tiempo', inplace=True)#rellenar los valores con 'Fallecido'



df['Pertenencia étnica'].fillna(6, inplace=True)#rellenar los(pocos 5) valores con 6



df['Nombre del grupo étnico'].fillna('Sin Comunidad', inplace=True)

unique_counts = {}
for column in df.columns:
    num_unique = df[column].nunique()
    if num_unique < 200 and num_unique>1:
        unique_counts[column] = num_unique

'''print("UNICOSSFDSFDSFSDFDSF")
print(unique_counts)
print(df['Unidad de medida de edad'].unique())
print(df.info())
print(df.describe())
'''

