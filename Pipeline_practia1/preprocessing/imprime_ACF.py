from sklearn.base import BaseEstimator, TransformerMixin
from statsmodels.tsa.stattools import acf
from statsmodels.graphics.tsaplots import plot_acf
import matplotlib.pyplot as plt
import pandas as pd

class imprime_ACF(BaseEstimator, TransformerMixin):
    def __init__(self, columns = None, nlags = 6, plot = True):
        self.columns = columns
        self.nlags = nlags
        self.plot = plot
    
    def fit(self, X, y = None):
        return self
    
    def transform(self, X):

        # Me aseguro que sea DF
        X_ = X if isinstance(X, pd.DataFrame) else pd.DataFrame(X) 
        # Trabaja con columnas numéricas                         
        cols = self.columns or X_.select_dtypes(include='number').columns.tolist()          
        
        X_features = X_.copy()

        filas = []

        for col in cols:
            # ACF con statsmodels
            acf_vals = acf(X_features[col].values, nlags=self.nlags, fft=True)
            # Agregar valores a una columna del dataset a mostrar
            for i, val in enumerate(acf_vals, start = 1):
                filas.append({'variable':col, 'lag': i, 'ACF':val})
              
            if self.plot:
                series = pd.to_numeric(X_[col], errors='coerce').dropna()
                plt.figure(figsize=(12,6))
                ax = plt.gca()  
                plot_acf(
                    series, 
                    lags = self.nlags, 
                    title = f'ACF {col}',
                    ax = ax,
                    alpha = 0.5,
                    use_vlines=True)
                ax.grid(True, linestyle='--', alpha=0.7)  # grilla más suave
                ax.set_xlabel('Rezago (lag)', fontsize=12)
                ax.set_ylabel('Autocorrelación', fontsize=12)
                plt.tight_layout()
                #plt.show()
                plt.savefig(f'img/acf_{col}.png')
                plt.close()

        
        df_acf = pd.DataFrame.from_records(filas)
        
        return df_acf
