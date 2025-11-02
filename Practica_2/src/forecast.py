import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import statsmodels.api as sm
from src.transformar import des_transformar
from src.evaluar import evaluar_forecast

def hacer_forecast(v1, h1, primer_valor, scaler, p=0, d=0, q=1, n_lags=7):

    # Convertir ventana a Serie con índice adecuado
    serie = pd.Series(v1.values.flatten(), index=v1.index)
    
    # Entrenar modelo ARIMA
    modelo = sm.tsa.SARIMAX(serie, order=(p,d,q),
                            enforce_stationarity=False,
                            enforce_invertibility=False)
    resultado = modelo.fit(disp=False)
    
    # Forecast en escala transformada
    h = len(h1)
    forecast_std = resultado.get_forecast(steps=h).predicted_mean
    
    # Destransformar a escala original
    forecast_original = des_transformar(forecast_std, primer_valor, scaler)

    y_true = np.array(h1.values).flatten()
    y_pred = np.array(forecast_original).flatten()

    medidas = evaluar_forecast(y_true, y_pred)

    for nombre, valor in medidas.items():
        print(f'{nombre} : {np.round(valor, 4)}')
    
    # Graficar
    n_ventana = len(v1)
    n_horizonte = len(h1)
    idx_ventana = np.arange(n_ventana)
    idx_horizonte = np.arange(n_ventana, n_ventana + n_horizonte)
    
    plt.figure(figsize=(14,6))
    plt.plot(idx_ventana, v1.values, label='Ventana histórica', color='blue', linewidth=2)
    plt.plot(idx_horizonte, h1.values, label='Horizonte real', color='green', linewidth=2)
    plt.plot(idx_horizonte, forecast_original, label='Forecast', color='red', linestyle='--', linewidth=2)
    plt.xlabel('Tiempo')
    plt.ylabel('Valores')
    plt.title('Ventana histórica, horizonte real y forecast (escala original)')
    plt.legend()
    plt.grid(alpha=0.3)
    plt.show()
    
    return forecast_original, resultado
