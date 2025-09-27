import numpy as np

def logaritmica(df, columnas = None, c = 0):
    '''
    Parámetros
    ----------
    df : pandas.DataFrame
        DataFrame de entrada con las series de tiempo.
    columnas : list of str, optional
        Lista de columnas a transformar. 
        Si no se especifica, se aplicará a todas las columnas excepto 'conteo'.
    c : float, default=0
        Constante que se suma a los valores antes de aplicar el logaritmo
        para evitar log(0) o log de valores negativos.

    Retorna
    -------
    pandas.DataFrame
        DataFrame con las columnas seleccionadas transformadas a escala logarítmica.
    '''
    df_log = df.copy()

    if columnas is None:
        columnas = [col for col in df.columns if col not in ['conteo']]

    df_log[columnas] = np.log(df_log[columnas] + c)    

    return df_log


def cuadrada(df, columnas = None):
    '''
    Eleva al cuadrado las columnas seleccionadas de un DataFrame.

    Parámetros:
    - df : pd.DataFrame
    - columnas : lista de columnas a transformar (default: todas menos 'conteo')

    Retorna:
    - pd.DataFrame con las columnas seleccionadas elevadas al cuadrado
    '''
    df_cuadrada = df.copy()

    if columnas is None:
        columnas = [col for col in df_cuadrada.columns if col not in ['conteo']]

    df_cuadrada[columnas] = df_cuadrada[columnas] ** 2
    
    return df_cuadrada

    