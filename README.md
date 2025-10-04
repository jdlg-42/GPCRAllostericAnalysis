# Computer-based identification of key residues in GPCR allosteric signaling
*Juandiego López González 2025*

This repository contains the Python scripts used for the Bachelor's Thesis **"Computer-based identification of key residues in GPCR allosteric signaling"** It provides tools to study allosteric sensitivity and perform attention-based analyses on allosteric residues using the protein language model **ESM-2** on the sequences of the **A2A adenosine receptor** and the **beta-2 adrenergic receptor**. It also includes tools to build and analyze amino acid contact graphs to identify residues with high betweenness centrality values. The goal is to detect key residues in allosteric communication in GPCRs.

## Installation

```bash
# Clone the repository
git clone https://github.com/yourusername/GPCRAllostericAnalysis.git
cd GPCRAllostericAnalysis

# Create conda environment (required for ESM-2)
conda create -n esm_env python=3.11
conda activate esm-env

# Install dependencies
pip install torch fair-esm numpy pandas tqdm scipy biopython igraph py3dMol
```

For Mac users, PyTorch with **MPS** support (instead of CUDA) is required:

```python
import torch
print(f"PyTorch version: {torch.__version__}")
print(f"Is MPS (M1) available? {torch.backends.mps.is_available()}")
print(f"Is CUDA available? {torch.cuda.is_available()}")  # Should be False on M1
```

Required modules:

* PyTorch
* scipy
* biopython
* igraph
* matplotlib
* numpy
* Py3DMol
* Seaborn

Scripts & Notebooks:

* **allosteric\_analyzer.py**: Defines the allosteric analyzer class. Enables the study of allosteric attention data from a given sequence.
* **analyze\_a2a.py**: Analysis script for the A2A adenosine receptor.
* **analyze\_adrb2.py**: Analysis script for the beta-2 adrenergic receptor.
* **pdb\_downloader.py**: Located inside the `PDB_files` directory. Allows downloading `.pdb` files directly into this directory for local structure analysis.
* **protein\_visualization.ipynb**: Jupyter Notebook for 3D visualization of protein structures and highlighting key residues involved in the effector binding site and G-protein binding.
* **distancias.py**: Script for building protein contact graphs and computing centrality data.

---

# Identifying Pairs of Residues with High Attention Toward the Allosteric Site Using ESM-2

The scripts **allosteric\_analyzer.py**, **analyze\_a2a.py**, and **analyze\_adrb2.py** are used to apply the analysis to the A2A adenosine and beta-2 adrenergic GPCRs. For each receptor, the attention heads with the highest allosteric impact are identified, and the **cumulative average attention** is calculated (a global measure of the attention that sequence residues give to the orthosteric site residues).

## Identifying Attention Heads with High Allosteric Impact

The paper by **Dong et al., 2024** proposes quantitative methods to compute the allosteric sensitivity of attention heads. This involves comparing the **global attention** toward the sequence (total activity) and the **specific attention** the model heads give to the allosteric site residues within the sequence (allosteric activity). From these values, the proportion of total activity attributable to allosteric activity can be calculated, known as the **allosteric impact**.

## Calculating Attention Toward Allosteric Site Residues

A metric called **cumulative average attention** is used.

---

## Usage

### Basic Analysis

```python
from allosteric_analyzer import AllosticHeadAnalyzer

# Create an analyzer instance
analyzer = AllosticHeadAnalyzer(threshold=0.3)

# Analyze a protein sequence
sequence = "MPIMGSSVYITVELAIAVLAILGNVLVCWAV..."  # Protein sequence
allosteric_sites = [85, 89, 246, 253]  # Allosteric site residues

# Store results
results = analyzer.analyze_protein(sequence, allosteric_sites)

# Access obtained values
impact_scores = results["impacts"].squeeze().tolist()
snr_values = results["snrs"].squeeze().tolist()
```

### Run Analysis on GPCRs

A2A adenosine receptor:

```bash
python analyze_a2a.py
```

Beta-2 adrenergic receptor:

```bash
python analyze_adrb2.py
```

---

# References

1. Dong et al. (2024). *Allo-Allo: Data-efficient prediction of allosteric sites*. bioRxiv. DOI: pending
2. ESM-2 Model: [https://github.com/facebookresearch/esm](https://github.com/facebookresearch/esm)
3. Allosteric Analyzer: [https://github.com/amoyag/allostery\_heads](https://github.com/amoyag/allostery_heads)

---

# Author and Publication Date

**Juandiego López González. June 2025**

---

Universidad de Málaga.
