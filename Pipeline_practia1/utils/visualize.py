import matplotlib.pyplot as plt

def plot_originalvsnormalizado(name, original, procesados, columnas=None, labels_procesados=None):
    if columnas is None:
        columnas = original.select_dtypes(include='number').columns.tolist()
    
    # Si no pasas labels, se usa un nombre por defecto
    if labels_procesados is None:
        labels_procesados = [f'Transformada {i+1}' for i in range(len(procesados))]

    for col in columnas:
        fig, ax = plt.subplots(figsize=(30, 6))

        # Graficar original
        ax.plot(original[col], color='purple', alpha=0.5, linewidth=2, label=f'Original: {col}')

        # Graficar procesados
        for i, procesado in enumerate(procesados):
            ax.plot(procesado[col], linewidth=2, label=labels_procesados[i])

        # Configuración estética
        ax.set_xlabel('Tiempo', fontsize=16)
        ax.set_ylabel('Valor', fontsize=16)
        ax.set_title(f'Normalización {col}', fontsize=16, fontweight='bold')
        ax.legend()
        ax.grid(True, linestyle='--', alpha=0.5)

        plt.tight_layout()
        plt.savefig(f"img/{name}_{col}.png")
        plt.show()

def plot_originalvsescalas(name, original, procesados, columnas=None, labels_procesados=None):
    if columnas is None:
        columnas = original.select_dtypes(include='number').columns.tolist()
    
    # Si no pasas labels, se usa un nombre por defecto
    if labels_procesados is None:
        labels_procesados = [f'Transformada {i+1}' for i in range(len(procesados))]

    for col in columnas:
        fig, ax = plt.subplots(figsize=(30, 6))

        # Graficar original
        ax.plot(original[col], color='purple', alpha=0.5, linewidth=2, label=f'Original: {col}')

        # Graficar procesados
        for i, procesado in enumerate(procesados):
            ax.plot(procesado[col], linewidth=2, label=labels_procesados[i])

        # Configuración estética
        ax.set_xlabel('Tiempo', fontsize=16)
        ax.set_ylabel('Valor', fontsize=16)
        ax.set_title(f'Escalas {col}', fontsize=16, fontweight='bold')
        ax.legend()
        ax.grid(True, linestyle='--', alpha=0.5)

        plt.tight_layout()
        plt.savefig(f"img/{name}_{col}.png")
        plt.show()

def plot_originalvsdiff(name, original, procesados, columnas=None, labels_procesados=None):
    if columnas is None:
        columnas = original.select_dtypes(include='number').columns.tolist()

    if labels_procesados is None:
        labels_procesados = [f'Diferenciaciones {i+1}' for i in range(len(procesados))]

    for col in columnas:
        fig, ax = plt.subplots(figsize=(30, 6))

        # Graficar original
        ax.plot(original[col], color='purple', alpha=0.5, linewidth=2, label=f'Original: {col}')

        # Graficar procesados
        for i, procesado in enumerate(procesados):
            ax.plot(procesado[col], linewidth=2, label=labels_procesados[i])

        # Configuración estética
        ax.set_xlabel('Tiempo', fontsize=16)
        ax.set_ylabel('Valor', fontsize=16)
        ax.set_title(f'Diferenciación {col}', fontsize=16, fontweight='bold')
        ax.legend()
        ax.grid(True, linestyle='--', alpha=0.5)

        plt.tight_layout()
        plt.savefig(f"img/{name}_{col}.png")
        plt.show()