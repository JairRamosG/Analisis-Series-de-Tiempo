import numpy as np

def remove_outliers_zscore(series, threshold=3):
    mean = np.mean(series)
    std = np.std(series)
    z_scores = (series - mean) / std
    cleaned_series = series[np.abs(z_scores) < threshold]
    return cleaned_series


def remove_outliers_iqr(df, variable, factor=1.5):
    Q1 = df[variable].quantile(0.25)
    Q3 = df[variable].quantile(0.75)
    IQR = Q3 - Q1
    lower_limit = Q1 - factor * IQR
    upper_limit = Q3 + factor * IQR
    
    df_clean = df[(df[variable] >= lower_limit) & (df[variable] <= upper_limit)]
    return df_clean

def reemplazar_por_media(df, variable):
    series = df[variable].copy()
    media = series.mean(skipna=True) 
    series.fillna(media, inplace=True) 
    return series
