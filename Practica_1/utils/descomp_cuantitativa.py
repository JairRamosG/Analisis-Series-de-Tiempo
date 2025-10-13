from statsmodels.tsa.seasonal import seasonal_decompose
import matplotlib.pyplot as plt

from statsmodels.tsa.seasonal import seasonal_decompose
import matplotlib.pyplot as plt

def tendencia(nombre, df, periodo, enfoque='additive'):
    """
    Grafica la serie original y su tendencia suavizada.

    Parámetros
    ----------
    nombre : str
        Columna del DataFrame con la serie de tiempo.
    df : pandas.DataFrame
        DataFrame con la serie de tiempo.
    periodo : int
        Número de observaciones por ciclo estacional.
    enfoque : str
        'additive' o 'multiplicative'.

    Retorna
    -------
    pandas.Series
        Serie de la tendencia.
    """
    descomposicion = seasonal_decompose(df[nombre], model=enfoque, period=periodo)
    tendencia = descomposicion.trend

    # Crear figura y eje
    fig, ax = plt.subplots(figsize=(30, 8))

    # Graficar serie original
    ax.plot(df[nombre], alpha=0.5, label='Serie original')

    # Graficar tendencia
    ax.plot(tendencia, color='red', linewidth=2, label='Tendencia')

    # Configuración estética
    ax.set_xlabel('Conteo', fontsize=16)
    ax.set_ylabel('Amplitud', fontsize=16)
    ax.set_yscale('log')  # si quieres logaritmo, si no quitar
    ax.set_title(f'Tendencia de {nombre}', fontsize=16, fontweight='bold')
    ax.legend()
    ax.grid(True, linestyle='--', alpha=0.5)

    plt.tight_layout()
    plt.savefig(f"img/3_{nombre}.png")
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
    plt.title('Estacionalidad mediante descomposición', fontsize=16, fontweight='bold')
    plt.legend()
    plt.show()

    return estacional