from pathlib import Path
import numpy as np
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt


def guardar_matriz_confusion(cm, modelo_nombre, output_dir):
    fig, ax = plt.subplots(figsize=(8, 6))
    
    # Dibujar matriz
    im = ax.imshow(cm, interpolation='nearest', cmap='Blues')
    ax.figure.colorbar(im, ax=ax)
    
    # Etiquetas
    classes = ['Clase 0\n(Open≤Close)', 'Clase 1\n(Open>Close)']
    ax.set(xticks=np.arange(2),
           yticks=np.arange(2),
           xticklabels=classes,
           yticklabels=classes,
           ylabel='Clase Real',
           xlabel='Clase Predicha',
           title=f'Matriz de Confusión - {modelo_nombre}')
    
    plt.setp(ax.get_xticklabels(), rotation=45, ha="right", rotation_mode="anchor")
    
    # Valores en celdas
    thresh = cm.max() / 2.
    for i in range(2):
        for j in range(2):
            ax.text(j, i, f'{cm[i, j]:,}',
                   ha="center", va="center",
                   color="white" if cm[i, j] > thresh else "black",
                   fontsize=14, fontweight='bold')
    
    fig.tight_layout()
    
    # Guardar
    output_path = Path(output_dir) / f"confusion_matrix_{modelo_nombre.lower().replace(' ', '_')}.png"
    plt.savefig(output_path, dpi=150, bbox_inches='tight')
    plt.close()
    
    print(f"  ✓ Guardado: {output_path}")
