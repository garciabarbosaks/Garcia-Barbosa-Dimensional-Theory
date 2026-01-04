"""
Implementación matemática de la Teoría de Dimensiones Perceptuales Alternantes
Autor: Kevin Sebastián García Barbosa
Fecha: Marzo 2024
"""

import numpy as np
import sympy as sp

class SecuenciaGarciaBarbosa:
    """Clase que implementa el patrón dimensional 1E-2E-3E-4T-5E-6T..."""
    
    def __init__(self, n_dim=11):
        """
        Inicializa la secuencia García-Barbosa
        
        Parámetros:
        -----------
        n_dim : int
            Número total de dimensiones (por defecto 11)
        """
        self.n_dim = n_dim
        self.secuencia = self._generar_secuencia()
        
    def _generar_secuencia(self):
        """Genera la secuencia E-E-E-T-E-T-E-T-E-T-E..."""
        sec = []
        for i in range(1, self.n_dim + 1):
            if i in [1, 2, 3, 5, 7, 9, 11]:
                sec.append(('D{}'.format(i), 'ESPACIO'))
            else:
                sec.append(('D{}'.format(i), 'TIEMPO'))
        return sec
    
    def mostrar_secuencia(self):
        """Muestra la secuencia completa"""
        print("Secuencia García-Barbosa:")
        print("-" * 40)
        for dim, tipo in self.secuencia:
            print(f"{dim}: {tipo}")
        print("-" * 40)
    
    def nivel_perceptivo(self, nivel):
        """
        Calcula las propiedades perceptuales de un ser de nivel n
        
        Parámetros:
        -----------
        nivel : int
            Nivel perceptual (2 para humanos, 3 para ser 5D, etc.)
            
        Retorna:
        --------
        dict : Diccionario con propiedades del nivel
        """
        if nivel < 2:
            raise ValueError("Nivel mínimo es 2 (seres 3D como nosotros)")
            
        k = 2 * nivel + 1  # Dimensiones espaciales habitadas
        tiempo = k + 1     # Su dimensión temporal
        
        return {
            'nivel': nivel,
            'dim_espaciales': k,
            'dim_temporal': tiempo,
            'dim_totales': k + 1,
            'dimensiones_habitadas': list(range(1, k + 1)),
            'tiempo_experiencial': tiempo,
            'nombre': self._nombre_nivel(nivel)
        }
    
    def _nombre_nivel(self, nivel):
        """Nombre descriptivo del nivel"""
        nombres = {
            2: "Ser 3D (Humanos)",
            3: "Ser 5D",
            4: "Ser 7D", 
            5: "Ser 9D",
            6: "Ser 11D"
        }
        return nombres.get(nivel, f"Ser de nivel {nivel}")
    
    def metrica_nivel(self, nivel):
        """
        Genera la métrica para un ser del nivel especificado
        
        La métrica tiene signatura: (+1, +1, ..., -1) donde el último
        elemento es la dimensión temporal experiencial
        """
        props = self.nivel_perceptivo(nivel)
        k = props['dim_espaciales']
        
        # Crear métrica diagonal
        g = np.diag([1] * k + [-1])
        
        return {
            'nivel': nivel,
            'dimensiones': k + 1,
            'metrica': g,
            'signatura': f"({k}, 1)"
        }
    
    def relacion_tiempo_espacio(self, nivel_inferior, nivel_superior):
        """
        Muestra cómo el tiempo de nivel n es espacio para nivel n+1
        """
        inf = self.nivel_perceptivo(nivel_inferior)
        sup = self.nivel_perceptivo(nivel_superior)
        
        tiempo_inf = inf['tiempo_experiencial']
        
        # Verificar que el tiempo del inferior está en las dimensiones
        # habitadas por el superior
        if tiempo_inf in sup['dimensiones_habitadas']:
            relacion = f"D{tiempo_inf} (tiempo de nivel {nivel_inferior}) = "
            relacion += f"espacio para nivel {nivel_superior}"
        else:
            relacion = f"No hay relación directa entre niveles {nivel_inferior} y {nivel_superior}"
        
        return relacion


# Ejemplo de uso
if __name__ == "__main__":
    print("=" * 60)
    print("TEORÍA DE DIMENSIONES PERCEPTUALES ALTERNADES")
    print("Implementación Matemática - Kevin S. García Barbosa")
    print("=" * 60)
    
    # Crear secuencia
    gb = SecuenciaGarciaBarbosa()
    gb.mostrar_secuencia()
    
    print("\n" + "=" * 60)
    print("PROPIEDADES POR NIVEL:")
    print("=" * 60)
    
    # Analizar cada nivel
    for nivel in range(2, 7):
        props = gb.nivel_perceptivo(nivel)
        print(f"\n{props['nombre']}:")
        print(f"  - Dimensiones espaciales habitadas: D1-D{props['dim_espaciales']}")
        print(f"  - Tiempo experiencial: D{props['tiempo_experiencial']}")
        print(f"  - Dimensiones totales: {props['dim_totales']}D")
        
        # Mostrar relación con nivel anterior
        if nivel > 2:
            rel = gb.relacion_tiempo_espacio(nivel-1, nivel)
            print(f"  - Relación: {rel}")
    
    print("\n" + "=" * 60)
    print("MÉTRICAS POR NIVEL (primeros elementos):")
    print("=" * 60)
    
    # Mostrar métricas
    for nivel in range(2, 5):  # Solo primeros 3 niveles por brevedad
        metrica_info = gb.metrica_nivel(nivel)
        print(f"\nNivel {nivel} (signatura {metrica_info['signatura']}):")
        print(f"Métrica (forma diagonal): diag{tuple(metrica_info['metrica'].diagonal())}")
    
    print("\n" + "=" * 60)
    print("PARADOJA DEL NIVEL 6 (Ser 11D):")
    print("=" * 60)
    
    # Analizar paradoja del nivel 6
    props_l6 = gb.nivel_perceptivo(6)
    print(f"\n{props_l6['nombre']}:")
    print(f"- Habita dimensiones: D1-D{props_l6['dim_espaciales']}")
    print(f"- Su tiempo sería: D{props_l6['tiempo_experiencial']}")
    print(f"- Problema: D{props_l6['tiempo_experiencial']} > 11, ¡no existe en la secuencia!")
    print("\nSolución requerida:")
    print("1. Extender a D12 como tiempo del nivel 6, o")
    print("2. Reinterpretar D11 como tiempo emergente, o")
    print("3. Aceptar que el ser 11D es atemporal")
    
    print("\n" + "=" * 60)
