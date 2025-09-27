def estandarizar(df, columnas = None):
    '''
    Parámetros
    ----------
    df : pandas.DataFrame
        DataFrame de entrada con las series de tiempo.
    columnas : list of str, optional
        Lista de columnas a estandarizar. 
        Si no se especifica, se aplicará a todas las columnas excepto 'conteo'.

    Retorna
    -------
    pandas.DataFrame
        DataFrame con las columnas seleccionadas estandarizadas
        (media ~0 y desviación estándar ~1). La columna 'conteo' se mantiene intacta.
    '''
    df_stand = df.copy()

    if columnas is None:
        columnas = [col for col in df.columns if col not in ['conteo']]
        
    df_stand[columnas] = (df[columnas] - df[columnas].mean()) / df[columnas].std()

    return df_stand