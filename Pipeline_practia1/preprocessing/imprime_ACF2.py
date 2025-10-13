from statsmodels.tsa.stattools import acf
from statsmodels.graphics.tsaplots import plot_acf
import matplotlib.pyplot as plt
import pandas as pd

def imprime_ACF(df, columnas, nlags, plot = True):
    
    df = df if isinstance(df, pd.DataFrame) else pd.DataFrame(df)
    columns = columnas or df.select_dtypes(include='number').columns.to_list()

    for col in columns:
        series = pd.to_numeric(df[col], errors = 'coerce').dropna()
        if series.empty:
            continue
        
        if plot:
            fig, ax = plt.subplots(figsize=(8, 4))
            plot_acf(series, lags=nlags, alpha=0.5, use_vlines=True, ax=ax)
            ax.grid(True, linestyle='--', alpha=0.7)
            ax.set_xlabel('Rezago (lag)', fontsize=12)
            ax.set_ylabel('Autocorrelación', fontsize=12)
            ax.set_title(f'ACF {col}', fontsize=14)
            plt.tight_layout()
            #plt.show()
            plt.close(fig)
