from preprocessing.normalizaciones import Normalizaciones
from preprocessing.estandarizaciones import Estandariacion
from preprocessing.diferenciaciones import Diferenciaciones
from preprocessing.escalas import Escala_potencia, Escala_raiz, Escala_log
from preprocessing.imprime_ACF import imprime_ACF

from utils.visualize import plot_originalvsnormalizado, plot_originalvsescalas, plot_originalvsdiff

from sklearn.pipeline import Pipeline
from pipelines.pipeline_normalizacion import pipeline_normalizacion

import pandas as pd


ruta1 = 'data/processed/battery_processed.csv'
df1 = pd.read_csv(ruta1)
print('df original -------------------------------------------------------------------')
print(df1.head())

columnas = ['temperature_battery'] #######----------------------> Es la característica con la que voy a estar trabajando.

# Implementación con PIPELINE de sklearn
pipeline1 = Pipeline([
    ('minmax_scaler', Normalizaciones(['temperature_battery']))
])
df1_scaled_01, df1_scaled_m11 = pipeline1.fit_transform(df1)
print('df escalado [0,1]-------------------------------------------------------------------')
print(df1_scaled_01.head())
#print('df escalado [-1,1]-------------------------------------------------------------------')
#print(df1_scaled_m11.head())

# Implementación desde la carpeta pipelines
pipeline2 = pipeline_normalizacion(columnas)
df1, df2 = pipeline2.fit_transform(df1)
print('df escalado [0,1] llamandolo desde pipelines-------------------------------------------------------------------')
print(df1.head())
#################################################################
# Estandarización
pipeline3 = Pipeline([
    ('Estandarizacion', Estandariacion(columnas))
])
df3_estandarizado = pipeline3.fit_transform(df1)
print('df estandarizado media = 0 y std = 1 llamandolo desde pipelines-------------------------------------------------------------------')
print(df3_estandarizado.head())
#################################################################
#Graficar Normalizaciónes
columnas = ['temperature_battery']
labels = ['[0,1]', '[-1,1]', 'estandarizado']
plot_originalvsnormalizado('Normalizacion y Estandarización', df1, [df1_scaled_01, df1_scaled_m11, df3_estandarizado], columnas = columnas, labels_procesados = labels)


###################################################################################################################################################
# Potencia

pipeline4 = Pipeline([
    ('potencia', Escala_potencia(columnas))
])
df_potencias = pipeline4.fit_transform(df1)
print('df ** 2 llamandolo desde pipelines-------------------------------------------------------------------')
print(df_potencias.head())

###################################################################################################################################################
# Raiz

pipeline5 = Pipeline([
    ('raiz', Escala_raiz(columnas))
])
df_raiz = pipeline5.fit_transform(df1)
print('df ** 1/2 llamandolo desde pipelines-------------------------------------------------------------------')
print(df_raiz.head())

###################################################################################################################################################
# Log

pipeline6 = Pipeline([
    ('log', Escala_log(columnas))
])
df_log = pipeline6.fit_transform(df1)
print('df Log llamandolo desde pipelines-------------------------------------------------------------------')
print(df_log.head())

#Graficar las escalas
labels = ['Cuadrada', 'Raiz', 'Log']
plot_originalvsescalas('Escalas', df1, [df_potencias, df_raiz, df_log], columnas = columnas, labels_procesados = labels)

###################################################################################################################################################
# Diferenciaciónes
num = 3
pipeline7 = Pipeline([
    ('diferenciaciones', Diferenciaciones(num, columnas))
])

df_diff_list = pipeline7.fit_transform(df1)
print('df diff llamandolo desde pipelines-------------------------------------------------------------------')
for i in df_diff_list:
    print(i.head())

#Graficar las escalas
labels = [f'diff {i}' for i in range(1, num+1)]
plot_originalvsdiff('Escalas', df1, df_diff_list, columnas = columnas, labels_procesados = labels)


#### Continuar con la ACF
nlags = 5
pipeline8 = Pipeline([
    ('ACF', imprime_ACF(columnas, nlags))
])
df_acf = pipeline8.fit_transform(df1)
print('df1 y ahora se le aplcia el ACF ----------------------------------------------------------------------')
print(df_acf.head())


