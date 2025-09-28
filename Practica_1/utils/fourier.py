import numpy as np
import matplotlib.pyplot as plt

def dom_freq(df, columna, fs=1.0, graficar=True):
    '''
    Calcula la transformada de Fourier y encuentra la frecuencia dominante.

    Parámetros
    ----------
    df : pd.DataFrame
        DataFrame con la serie temporal.
    columna : str
        Nombre de la columna a transformar.
    fs : float, opcional
        Frecuencia de muestreo (default=1.0).
    graficar : bool, opcional
        Si True, grafica el espectro (default=True).

    Retorna
    -------
    frecuencias : np.ndarray
        Vector de frecuencias físicas (Hz).
    espectro : np.ndarray
        Magnitud del espectro de Fourier.
    freq_dominante : float
        Frecuencia dominante (Hz).
    amp_dominante : float
        Amplitud de la frecuencia dominante.
    '''
    
    x = df[columna].values
    x = x[~np.isnan(x)] 

    N = len(x)
    X = np.fft.fft(x)
    espectro = np.abs(X) / N  
    
    frecuencias = np.fft.fftfreq(N, d=1/fs)
    
    frec_positivas = frecuencias[:N//2]
    espectro_positivo = espectro[:N//2]
    
    idx_dominante = np.argmax(espectro_positivo[1:]) + 1  
    freq_dominante = frec_positivas[idx_dominante]
    amp_dominante = espectro_positivo[idx_dominante]
    
    if graficar:
        plt.figure(figsize=(12, 5))
        plt.plot(frec_positivas, espectro_positivo, color='orange', label='Espectro')
        plt.axvline(freq_dominante, color='red', linestyle='--', 
                   label=f'Frec. dominante: {freq_dominante:.4f} Hz')
        plt.xlabel('Frecuencia (Hz)')
        plt.ylabel('Amplitud')
        plt.title(f'Espectro de Frecuencia - {columna}')
        plt.legend()
        plt.grid(True)
        plt.show()
    
    return frec_positivas, espectro_positivo, freq_dominante, amp_dominante