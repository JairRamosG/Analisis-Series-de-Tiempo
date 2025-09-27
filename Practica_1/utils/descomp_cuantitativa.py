from statsmodels.tsa.seasonal import seasonal_decompose
import matplotlib.pyplot as plt

def tendencia(nombre, df, periodo, enfoque):
    '''
        Parámetros
    ----------
    nombre : str
        Nombre de la columna del DataFrame que contiene la serie de tiempo.
    df : pandas.DataFrame
        DataFrame que contiene la serie de tiempo.
    periodo : int
        Frecuencia de la serie para la descomposición (número de observaciones
        que forman un ciclo estacional).
    enfoque : str
        Puede ser aditivo o multiplicativo.

    Retorna
    -------
    None
        Muestra un gráfico de la serie original y su tendencia suavizada.
    '''
    # Tendencia de la serie
    descomposicion = seasonal_decompose(df[nombre], model= enfoque , period=periodo)
    tendencia = descomposicion.trend
    
    tendencia.plot(
    figsize=(30,8),
    color = 'red',
    label = 'Tendencia')

    # Serie original
    plt.plot(df[nombre], alpha=0.5, label='Original')
    plt.xlabel('Conteo')
    plt.ylabel(nombre)
    plt.title('Tendencia mediante descomposición')
    plt.legend()
    plt.show()

    return tendencia

def estacionalidad(nombre, df, periodo, enfoque):
    '''
        Parámetros
    ----------
    nombre : str
        Nombre de la columna del DataFrame que contiene la serie de tiempo.
    df : pandas.DataFrame
        DataFrame que contiene la serie de tiempo.
    periodo : int
        Frecuencia de la serie para la descomposición (número de observaciones
        que forman un ciclo estacional).

    Retorna
    -------
    None
        Muestra un gráfico de la serie original y su estacionalidad.
    '''
    # Estacionalidad de la serie
    descomposicion = seasonal_decompose(df[nombre], model=enfoque, period=periodo)
    estacional = descomposicion.seasonal

    plt.figure(figsize=(30, 8))
    plt.plot(estacional, color='orange', label='Estacionalidad')
    # plt.plot(df[nombre], alpha=0.5, label='Original')
    plt.xlabel('Conteo')
    plt.ylabel(nombre)
    plt.title('Estacionalidad mediante descomposición')
    plt.legend()
    plt.show()

    return estacional