def diferenciar(df, num, columnas = None):
    '''
    Parámetros
    ----------
    df : pandas.DataFrame
        DataFrame de entrada con las series de tiempo.
    num : int
        Orden de la diferenciación (1 = primera diferencia, 2 = segunda, etc.).
    columnas : list of str, optional
        Lista de columnas a diferenciar. 
        Si no se especifica, se aplicará a todas las columnas excepto 'conteo'.

    Retorna
    -------
    pandas.DataFrame
        DataFrame con las columnas seleccionadas diferenciadas.
        La columna 'conteo' se mantiene intacta.
    '''
    df_diff = df.copy()

    if columnas is None:
        columnas = [col for col in df.columns if col not in ['conteo']]

    df_diff[columnas] = df[columnas].diff(num)


    return df_diff