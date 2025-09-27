def normalizar_0_1(df, columnas = None):
    '''
    Parámetros
    ----------
    df : pandas.DataFrame
        DataFrame de entrada con las series de tiempo.
    columnas : list of str, optional
        Lista de columnas a normalizar. 
        Si no se especifica, se aplicará a todas las columnas excepto 'conteo'.

    Retorna
    -------
    pandas.DataFrame
        DataFrame con las columnas seleccionadas normalizadas al rango [0, 1].
    '''
    df_norm = df.copy()

    if columnas is None:
        columnas = [col for col in df.columns if col not in ['conteo']]
    df_norm[columnas] = (df[columnas] - df[columnas].min()) / (df[columnas].max() - df[columnas].min())

    return df_norm

def normalizar_neg1_1(df, columnas = None):
    '''
    Parámetros
    ----------
    df : pandas.DataFrame
        DataFrame de entrada con las series de tiempo.
    columnas : list of str, optional
        Lista de columnas a normalizar. 
        Si no se especifica, se aplicará a todas las columnas excepto 'conteo'.

    Retorna
    -------
    pandas.DataFrame
        DataFrame con las columnas seleccionadas normalizadas al rango [-1, 1].
    '''
    df_norm = df.copy()

    if columnas is None:
        columnas = [col for col in df.columns if col not in ['conteo']]

    df_norm[columnas] = ((df[columnas] - df[columnas].min()) / (df[columnas].max() - df[columnas].min()) * 2) - 1

    return df_norm