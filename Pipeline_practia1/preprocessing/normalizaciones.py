from sklearn.base import BaseEstimator, TransformerMixin
import pandas as pd

class Normalizaciones(BaseEstimator, TransformerMixin):

    def __init__(self, columns = None):
        self.columns = columns

    def fit(self, X, y = None):
        # Convertir a DF si es un array
        X_ = X if isinstance(X, pd.DataFrame) else pd.DataFrame(X)

        if self.columns is None:
            self.columns = X_.select_dtypes(include='number').columns.tolist()

        # Guardar los parametros aprendidos en el fit
        self.min_ = X_[self.columns].min()
        self.max_ = X_[self.columns].max()        
        return self
    
    def transform(self, X):
        # Normalizacion [01]
        X01_ = X.copy()
        X01_[self.columns] = (X01_[self.columns] - self.min_)/(self.max_ - self.min_)

        # Normalizacion [-1,1]
        Xm11_ = X.copy()
        Xm11_[self.columns] = ((Xm11_[self.columns] - self.min_)/(self.max_ - self.min_)) * 2 - 1 

        return X01_, Xm11_

