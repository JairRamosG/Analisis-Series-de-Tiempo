from sklearn.base import BaseEstimator, TransformerMixin
import pandas as pd
import numpy as np

class Escala_potencia(BaseEstimator, TransformerMixin):
    
    def __init__(self, columns = None):
        self.columns = columns

    def fit(self, X, y = None):
        # COnvertir a df por si es una serie
        X_ = X if isinstance(X, pd.DataFrame) else pd.DataFrame(X)

        if self.columns is None:
            self.columns = X_.select_dtypes(include='number').columns.tolist()
        return self
    
    def transform(self, X):
        # POtencia
        Xpot_ = X.copy()
        Xpot_[self.columns] = Xpot_[self.columns] ** 2
        return Xpot_

class Escala_raiz(BaseEstimator, TransformerMixin):
    
    def __init__(self, columns = None):
        self.columns = columns

    def fit(self, X, y = None):
        # COnvertir a df por si es una serie
        X_ = X if isinstance(X, pd.DataFrame) else pd.DataFrame(X)

        if self.columns is None:
            self.columns = X_.select_dtypes(include='number').columns.tolist()
        return self
    
    def transform(self, X):
        # POtencia
        Xpot_ = X.copy()
        Xpot_[self.columns] = Xpot_[self.columns] ** (1/2)
        return Xpot_

class Escala_log(BaseEstimator, TransformerMixin):
    
    def __init__(self, columns = None):
        self.columns = columns

    def fit(self, X, y = None):
        # COnvertir a df por si es una serie
        X_ = X if isinstance(X, pd.DataFrame) else pd.DataFrame(X)

        if self.columns is None:
            self.columns = X_.select_dtypes(include='number').columns.tolist()
        return self
    
    def transform(self, X):
        # POtencia
        Xpot_ = X.copy()
        Xpot_[self.columns] = np.log1p(Xpot_[self.columns])
        return Xpot_