import numpy as np
from sklearn.metrics import mean_squared_error

def evaluar_forecast(y_true, y_pred):

    y_true = np.array(y_true)
    y_pred = np.array(y_pred)
    
    # RMSE
    rmse = np.sqrt(mean_squared_error(y_true, y_pred))
    
    # SMAPE
    smape_val = 100/len(y_true) * np.sum(2 * np.abs(y_pred - y_true) / (np.abs(y_true) + np.abs(y_pred)))
    
    # r^2 de Pearson
    r2_pearson = np.corrcoef(y_true, y_pred)[0,1] ** 2
    
    return {'RMSE': rmse,
            'SMAPE': smape_val,
            'R2_Pearson': r2_pearson}
