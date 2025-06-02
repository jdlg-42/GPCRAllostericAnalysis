# TFG: " " 
Juandiego López González 2025
En este repositorio se pueden encontrar los scripts de Python utilizados para realizar los estudios del TFG " ". En este repositorio se podrán encontrar herramientas para estudiar la sensibilidad alostérica y realizar estudios de atención sobre residuos alostérico empleando el modelo de lenguaje de proteínas ESM-2 en los GPCR A2A de adenosina y beta-2 adrenérgico. También contiene herramientas para construir y analizar los grafos de contacto de las proteínas para obtener residuos con valores de alta centralidad de intermediación, y empleando métodos para usar los datos de atención en dicho análisis. 

## Instalación

```bash
# Clonar el repositorio
git clone https://github.com/yourusername/TFG.git
cd allostery_heads

# Crear entorno de conda, necesario para usar ESM-2
conda create -n esm_env python=3.11 
conda activate esm-env

# Instalar las dependencias necesarias
pip install torch fair-esm numpy pandas tqdm scipy biopython igraph py3dMol
```
Para usuarios de Mac se requiere de PyTorch con soporte para MPS en vez de CUDA

```python
import torch
print(f"PyTorch version: {torch.__version__}")
print(f"Is MPS (M1) available? {torch.backends.mps.is_available()}")
print(f"Is CUDA available? {torch.cuda.is_available()}")  # Should be False on M1
```



Módulos necesarios:

- Pytorch
- scipy
- biopython
- igraph
- matplotlib
- numpy
- Py3DMol
- Seaborn

Scripts:
- allosteric_analyzer.py: código que define la clase de analizador alostérico. Permite estudiar los datos de atención alostérica a partir de una secuencia dada
- analyze_a2a.py: script de análisis del receptor A2A de adenosina.
- analyze_adrb2.py: script de análisis del receptor beta-2 adrenérgico.
- pdb_downloader.py: está dentro de un directorio PDB_files. Permite descargar archivos .pdb directamente a dicho directorio para trabajar localmente con las estructuras.
- protein_visualization.ipynb: es un Jupyter Notebook que permite realizar la visualización en 3D de la estructura de la proteína y resaltar los residuos de interés que componen el sitio de unión al efector y los que se unen a la proteína G.
- distancias.py: script para construir grafos de contacto de proteínas y obtener los datos de la centralidad. 

# Identificación de pares de residuos de alta atención hacia el sitio alostérico usando ESM-2

Se utilizan los scripts: allosteric_analyzer.py, para definir la clase del analizador, y analyze_a2a.py y analyze_adrb2 para aplicar el análisis a los GPCR A2A de adenosina y beta-2 adrenérgico. Para cada uno se determinan las cabezas de atención con alto impacto alostérico y se calcula la atención promedio acumulada (cálculo de la atención global que los residuos de la secuencia le prestan a los residuos del sitio ortostérico).

## Obtención de las cabezas de atención con alto impacto alostérico

El artículo de Dong et al., 2024 establece métodos cuantitativos para realizar el cálculo de la sensibilidad alostérica de las cabezas de atención. Esto se realiza a partir de la comparación de la atención global hacia la secuencia (actividad total) y la atención específica que las cabezas del modelo prestan a los residuos del sitio alostérico dentro de la secuencia (actividad alostérica). Con ambos valores se puede calcular la proporción de la actividad total que se debe a la actividad alostérica, lo que se conoce como impacto alostérico. 

## Cálculo de la atención hacia los residuos del sitio alostérico

Se utiliza una métrica llamada atención promedio acumulada.

## Uso

### Análisis básico

```python
from allosteric_analyzer import AllosticHeadAnalyzer

# Generar una instancia del analizador
analyzer = AllosticHeadAnalyzer(threshold=0.3)

# Analizar la secuencia de una proteína
sequence = "MPIMGSSVYITVELAIAVLAILGNVLVCWAV..."  # La secuencia de la proteína de interés
allosteric_sites = [85, 89, 246, 253]  # Los residuos del sitio alostérico 

# Guardar los resultados en una variable
results = analyzer.analyze_protein(sequence, allosteric_sites)

# Acceder a los valores obtenidos
impact_scores = results["impacts"].squeeze().tolist()
snr_values = results["snrs"].squeeze().tolist()
```

### Ejecutar el resultado en los GPCR

Receptor A2A de adenosina:

```bash
python analyze_a2a.py
```

Receptor beta-2 adrenérgico:

```bash
python analyze_adrb2.py
```

# Referencias

1. Dong et al. (2024). Allo-Allo: Data-efficient prediction of allosteric sites. bioRxiv. DOI: pending
2. ESM2 Model: https://github.com/facebookresearch/esm
3. Allosteric Analyzer: https://github.com/amoyag/allostery_heads

# Autor y fecha de publicación

Juandiego López González. Junio 2025
