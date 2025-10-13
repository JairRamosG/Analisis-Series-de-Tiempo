from sklearn.pipeline import Pipeline
from preprocessing.normalizaciones import Normalizaciones

def pipeline_normalizacion(columnas):
    pipeline = Pipeline([
        ('minmax_01', Normalizaciones(columns=columnas))
    ])
    return pipeline