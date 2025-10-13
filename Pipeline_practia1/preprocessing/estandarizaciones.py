from sklearn.base import BaseEstimator, TransformerMixin
import pandas as pd

class Estandariacion(BaseEstimator, TransformerMixin):

    def __init__(self, columns = None):
        self.columns = columns
    
    def fit(self, X, y = None):
        # Convertir a DF por si es un Array
        X_ = X if isinstance(X, pd.DataFrame) else pd.DataFrame(X)

        if self.columns is None:
            self.colums = X_.select_dtypes(include='number').columns.tolist()
        
        # Guardar lo que se ocupa del fit
        self.mean_ = X_[self.columns].mean()
        self.std_ = X_[self.columns].std()
        return self
    
    def transform(self, X):
        # Estandarización
        Xstd_ = X.copy() 
        Xstd_[self.columns] = (Xstd_[self.columns] - self.mean_) / self.std_
        return Xstd_