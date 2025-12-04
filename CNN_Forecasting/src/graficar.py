import matplotlib.pyplot as plt

def graficar_serie(df, variable, color='tab:blue', titulo=None):
    plt.figure(figsize=(18, 9))
    
    # Series plot
    plt.plot(df.index, df[variable], linewidth=2, marker='o', markersize=4, alpha=0.8, color=color, label=variable)
    
    # Grid estético
    plt.grid(True, linestyle='--', alpha=0.4)
    
    # Título dinámico si no se especifica uno
    if titulo:
        plt.title(titulo, fontsize=20, fontweight='bold')
    else:
        plt.title(f"Serie de tiempo: {variable}", fontsize=20, fontweight='bold')
    
    # Etiquetas de ejes
    plt.xlabel("Tiempo", fontsize=14)
    plt.ylabel(variable, fontsize=14)
    
    # Mejorado en ticks
    plt.xticks(rotation=45, fontsize=12)
    plt.yticks(fontsize=12)
    
    # Quitar bordes molestos
    for spine in ['top', 'right']:
        plt.gca().spines[spine].set_visible(False)
        
    # Auto legenda
    plt.legend(fontsize=13)
    
    plt.tight_layout()
    plt.show()