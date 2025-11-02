import pandas as pd
import matplotlib.pyplot as plt

from src.estandarizacion import estandarizar
from src.outliers import remove_outliers_iqr
from src.graficar import graficar_serie

from statsmodels.graphics.tsaplots import plot_acf, plot_pacf
import pmdarima as pm
import statsmodels.api as sm
from statsmodels.stats.diagnostic import acorr_ljungbox

import statsmodels.api as sm
from statsmodels.graphics.tsaplots import plot_acf, plot_pacf
from statsmodels.stats.diagnostic import acorr_ljungbox
import matplotlib.pyplot as plt
import numpy as np

def ARIMA_experimento(serie, p, d, q, n_lags=20):

    # Asegurar que no haya NaNs
    serie = serie.dropna()

    # Construcción del modelo
    modelo = sm.tsa.SARIMAX(serie, order=(p, d, q),
                            enforce_stationarity=False,
                            enforce_invertibility=False)
    resultado = modelo.fit(disp=False)

    print(f"\n Modelo ARIMA({p},{d},{q}) entrenado exitosamente\n")
    print(resultado.summary())

    residuos = resultado.resid

    # ========== Gráfica de residuos ==========
    plt.figure(figsize=(14,5))
    plt.plot(residuos, linewidth=1)
    plt.title(f'Residuos del modelo ARIMA({p},{d},{q})')
    plt.grid(alpha=0.35)
    plt.show()

    # ========== ACF ==========
    plt.figure(figsize=(14,4))
    plot_acf(residuos, lags=n_lags)
    plt.title('ACF - Residuos')
    plt.grid(alpha=0.35)
    plt.show()

    # ========== PACF ==========
    plt.figure(figsize=(14,4))
    plot_pacf(residuos, lags=n_lags, method='ywm')
    plt.title('PACF - Residuos')
    plt.grid(alpha=0.35)
    plt.show()

    # ========== Ljung - Box ==========
    print("\n Test de Ljung - Box ¿Es ruido blanco?\n")
    lb_test = acorr_ljungbox(residuos, 
                            lags=[lag for lag in range(1, n_lags + 1)], 
                            return_df=True)
    
    print(lb_test)  

    print('\n Interpretacion de la Hipótesis nula\n')

    for i in range(len(lb_test)):
        pval = lb_test['lb_pvalue'].iloc[i] 
        lag = lb_test.index[i]

        if pval < 0.05:
            print(f'Lag {lag}: Rechaza Ho, acepta H1 -- Hay correlación en los residuos')
        else:
            print(f'Lag {lag}: No rechaza Ho -- Residuos se comportan como ruido blanco')

    return resultado, residuos
