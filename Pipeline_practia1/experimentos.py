from preprocessing.normalizaciones import Normalizaciones
from preprocessing.diferenciaciones import Diferenciaciones
import pandas as pd
from statsmodels.graphics.tsaplots import plot_acf, plot_pacf
import matplotlib.pyplot as plt


ruta1 = 'data/processed/battery_processed.csv'
df = pd.read_csv(ruta1, index_col=0)
columna = ['temperature_battery'] 
nlags = 5

print('''
########################################################
#       Experimento 1 - PACF -> diff(2) -> PACF
########################################################''')

# ACF de datos originales
print('--------------- DataFrame ORIGINAL ---------------')
print(df.head())
print('--------------- Primer PACF ---------------')
plot_pacf(df[columna].dropna(), lags=5)
plt.show()

# Diferenciar
normalizador = Diferenciaciones(2, columna)
df_diff = normalizador.fit_transform(df)
df_diff = df_diff[-1]

# ACF de datos originales
print('------------- DataFrame DIFERENCIADO(2) ---------------')
print(df_diff.head())
print('--------------- Segundo PACF ---------------')
plot_pacf(df_diff[columna].dropna(), lags=5)
plt.show()

print('''
########################################################
#       Experimento 2 - ACF -> diff(2) -> ACF
######################################################## ''')

# ACF de datos originales
print('--------------- DataFrame ORIGINAL ---------------')
print(df.head())
print('--------------- Primer ACF ---------------')
plot_acf(df[columna].dropna(), lags=5)
plt.show()


# Normalizar
normalizador = Diferenciaciones(2, columna)
df_diff = normalizador.fit_transform(df)
df_diff = df_diff[-1]

# ACF de datos originales
print('------------- DataFrame DIFERENCIADO(2) ---------------')
print(df_diff.head())
print('--------------- Segundo ACF ---------------')
plot_acf(df_diff[columna].dropna(), lags=5)
plt.show()




