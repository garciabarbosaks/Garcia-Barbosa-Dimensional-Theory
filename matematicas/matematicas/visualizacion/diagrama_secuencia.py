"""
Generador de diagramas para la GB-Theory
Autor: Kevin Sebastián García Barbosa
"""

import matplotlib.pyplot as plt
import numpy as np

def crear_diagrama_secuencia():
    """Crea diagrama visual de la secuencia García-Barbosa"""
    
    fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(14, 6))
    
    # Configuración general
    plt.rcParams.update({'font.size': 10})
    
    # --- DIAGRAMA 1: Secuencia dimensional ---
    dimensiones = list(range(1, 12))
    tipos = ['E', 'E', 'E', 'T', 'E', 'T', 'E', 'T', 'E', 'T', 'E']
    colores = ['skyblue' if t == 'E' else 'lightcoral' for t in tipos]
    
    # Crear barras
    bars = ax1.bar([str(d) for d in dimensiones], 
                   [1]*11, 
                   color=colores,
                   edgecolor='black')
    
    # Añadir etiquetas
    for i, (bar, tipo) in enumerate(zip(bars, tipos)):
        ax1.text(bar.get_x() + bar.get_width()/2, 0.5,
                f'D{dimensiones[i]}\n({tipo})',
                ha='center', va='center', fontweight='bold')
    
    ax1.set_title('Secuencia García-Barbosa\n1E-2E-3E-4T-5E-6T-7E-8T-9E-10T-11E', 
                 fontsize=12, fontweight='bold')
    ax1.set_ylabel('')
    ax1.set_ylim(0, 1.2)
    ax1.set_yticks([])
    ax1.grid(axis='y', alpha=0.3)
    
    # Leyenda
    ax1.text(0.02, 0.98, 'E = Dimensión Espacial\nT = Dimensión Temporal',
            transform=ax1.transAxes, verticalalignment='top',
            bbox=dict(boxstyle='round', facecolor='wheat', alpha=0.5))
    
    # --- DIAGRAMA 2: Jerarquía perceptual ---
    niveles = ['L2\n(Ser 3D)', 'L3\n(Ser 5D)', 'L4\n(Ser 7D)', 'L5\n(Ser 9D)', 'L6\n(Ser 11D)']
    dim_esp = [3, 5, 7, 9, 11]
    tiempos = [4, 6, 8, 10, '¿12?']
    
    y_pos = np.arange(len(niveles))
    
    # Barras para dimensiones espaciales
    bars_esp = ax2.barh(y_pos, dim_esp, color='skyblue', 
                       edgecolor='black', label='Dim. Espaciales')
    
    # Marcadores para tiempos
    for i, (y, t) in enumerate(zip(y_pos, tiempos)):
        ax2.text(dim_esp[i] + 0.5, y, f'Tiempo: D{t}', 
                va='center', fontweight='bold')
    
    ax2.set_yticks(y_pos)
    ax2.set_yticklabels(niveles, fontweight='bold')
    ax2.set_xlabel('Número de Dimensiones Espaciales')
    ax2.set_title('Jerarquía de Niveles Perceptuales', 
                 fontsize=12, fontweight='bold')
    ax2.grid(axis='x', alpha=0.3)
    ax2.set_xlim(0, 13)
    
    # Añadir líneas de conexión para mostrar relación
    for i in range(len(niveles)-1):
        ax2.annotate('', xy=(dim_esp[i+1], y_pos[i+1]), 
                    xytext=(dim_esp[i], y_pos[i]),
                    arrowprops=dict(arrowstyle='->', 
                                   color='red', 
                                   lw=1.5,
                                   connectionstyle="arc3,rad=-0.2"))
    
    ax2.text(11.5, 4, 'Paradoja:\nSin D12', 
            ha='center', va='center',
            bbox=dict(boxstyle='round', facecolor='lightcoral', alpha=0.7))
    
    # Ajustar layout
    plt.tight_layout()
    
    # Guardar figura
    plt.savefig('diagrama_secuencia_gb.png', dpi=300, bbox_inches='tight')
    plt.savefig('diagrama_secuencia_gb.pdf', bbox_inches='tight')
    
    print("Diagrama guardado como 'diagrama_secuencia_gb.png' y '.pdf'")
    print("Resolución: 300 DPI - Listo para publicación")
    
    plt.show()

def crear_diagrama_relaciones():
    """Diagrama de cómo el tiempo de un nivel es espacio del siguiente"""
    
    fig, ax = plt.subplots(figsize=(10, 8))
    
    # Configurar ejes
    ax.set_xlim(0, 10)
    ax.set_ylim(0, 10)
    ax.set_aspect('equal')
    ax.axis('off')
    
    # Posiciones de los niveles
    posiciones = {
        'L2': (2, 2),
        'L3': (5, 4),
        'L4': (8, 6),
        'D4': (3.5, 3),
        'D6': (6.5, 5),
        'D8': (9.5, 7)
    }
    
    # Dibujar niveles como círculos
    for nivel, (x, y) in posiciones.items():
        if nivel.startswith('L'):
            color = 'lightblue'
            radio = 0.8
            # Círculo
            circle = plt.Circle((x, y), radio, color=color, 
                               ec='black', lw=2, alpha=0.7)
            ax.add_patch(circle)
            # Texto
            ax.text(x, y, nivel, ha='center', va='center', 
                   fontweight='bold', fontsize=12)
    
    # Dibujar dimensiones como rectángulos
    for dim, (x, y) in posiciones.items():
        if dim.startswith('D'):
            color = 'lightcoral'
            width, height = 1.2, 0.6
            # Rectángulo
            rect = plt.Rectangle((x - width/2, y - height/2), 
                                width, height, 
                                color=color, ec='black', lw=2, alpha=0.7)
            ax.add_patch(rect)
            # Texto
            ax.text(x, y, dim, ha='center', va='center', 
                   fontweight='bold', fontsize=11)
    
    # Conexiones y flechas
    conexiones = [
        ('L2', 'D4', 'Nuestro\ntiempo'),
        ('D4', 'L3', 'Espacio\npara L3'),
        ('L3', 'D6', 'Tiempo\nde L3'),
        ('D6', 'L4', 'Espacio\npara L4')
    ]
    
    for origen, destino, texto in conexiones:
        x1, y1 = posiciones[origen]
        x2, y2 = posiciones[destino]
        
        # Línea con flecha
        ax.annotate('', xy=(x2, y2), xytext=(x1, y1),
                   arrowprops=dict(arrowstyle='->', 
                                  color='green', 
                                  lw=2,
                                  connectionstyle="arc3,rad=0.2"))
        
        # Texto en medio
        mid_x = (x1 + x2) / 2
        mid_y = (y1 + y2) / 2
        ax.text(mid_x, mid_y + 0.3, texto, 
               ha='center', va='center',
               fontsize=9, 
               bbox=dict(boxstyle='round', facecolor='white', alpha=0.8))
    
    # Título
    ax.text(5, 9, 'RELACIÓN TIEMPO-ESPACIO ENTRE NIVELES\n"Mi tiempo es tu espacio"',
           ha='center', va='center', fontsize=14, fontweight='bold')
    
    # Leyenda explicativa
    leyenda_texto = (
        'Principio Fundamental:\n'
        'El tiempo experiencial de un nivel n\n'
        'es una dimensión espacial para el nivel n+1\n'
        '\n'
        'Ejemplo:\n'
        '• D4 es nuestro tiempo (L2)\n'
        '• D4 es espacio para L3 (ser 5D)'
    )
    
    ax.text(1, 7, leyenda_texto, ha='left', va='top',
           fontsize=10,
           bbox=dict(boxstyle='round', facecolor='lightyellow', alpha=0.8))
    
    plt.tight_layout()
    plt.savefig('relaciones_tiempo_espacio.png', dpi=300, bbox_inches='tight')
    print("Diagrama de relaciones guardado como 'relaciones_tiempo_espacio.png'")
    plt.show()

if __name__ == "__main__":
    print("Generando diagramas para la GB-Theory...")
    crear_diagrama_secuencia()
    crear_diagrama_relaciones()
    print("\n¡Diagramas generados exitosamente!")
    print("Inclúyelos en tu artículo y presentaciones.")
