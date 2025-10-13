from sklearn.base import BaseEstimator, TransformerMixin
import pandas as pd

class Diferenciaciones(BaseEstimator, TransformerMixin):
    
    def __init__(self, n, columns = None):
        self.n = n
        self.columns = columns        
    
    def fit(self, X, y=None):
        #Verificar que sea un DF
        X_ = X if isinstance(X, pd.DataFrame) else pd.DataFrame(X)

        if self.columns is None:
            self.columns = X_.select_dtypes(include='number').columns.tolist()
        return self
    
    def transform(self, X):
        X_ = X.copy()
        diferencias = [] 
        Xprev_ = X_.copy()

        for i in range(1, self.n+1):
            X_diff = Xprev_[self.columns].diff().reindex(X_.index)
            diferencias.append(X_diff)
            Xprev_ = X_diff
        return diferencias


        