from sklearn.preprocessing import StandardScaler
from src.outliers import reemplazar_por_media
import numpy as np
import pandas as pd

def transformar(v1, variable):
    serie_diff = v1.diff(1)
    
    media_diff = serie_diff.mean()
    serie_limpia = reemplazar_por_media(serie_diff, variable)
    
    scaler = StandardScaler()
    serie_estandarizada = scaler.fit_transform(serie_limpia.values.reshape(-1,1)).flatten()

    primer_valor = v1.iloc[0]
    serie_transformada = serie_estandarizada.copy()
    
    return serie_transformada, scaler, media_diff, primer_valor

def des_transformar(forecast_std, primer_valor, scaler):

    forecast_std = forecast_std.values if isinstance(forecast_std, pd.Series) else np.array(forecast_std)
    
    forecast_diff = scaler.inverse_transform(forecast_std.reshape(-1,1)).flatten()
    primer_valor = primer_valor if np.isscalar(primer_valor) else primer_valor.item()
    forecast_original = np.cumsum(forecast_diff) + primer_valor
    
    return forecast_original
