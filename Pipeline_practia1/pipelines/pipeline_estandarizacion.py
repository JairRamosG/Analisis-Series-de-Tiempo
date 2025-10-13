from sklearn.pipeline import Pipeline
from preprocessing.estandarizaciones import Estandariacion

def pipeline_estandarizacion(columnas):
    pipeline = Pipeline([
        ('estandarizacion', Estandariacion(columns=columnas))
    ])
    return pipeline