# Mathematicians' Legacy: Computational Explorations

This repository showcases great mathematicians through Jupyter notebooks blending historical narratives, mathematical theory, and Python implementations. Designed for academics, data scientists, and math enthusiasts, it brings timeless mathematical ideas to life.

## Project Overview
Each mathematician’s section includes:
- **Historical Biography**: Detailed narratives of their life and impact.
- **Mathematical Concepts**: Theorems and formulas in LaTeX.
- **Code Implementations**: Python scripts using mpmath, SymPy, and matplotlib.
- **Visualizations**: Plots illustrating mathematical patterns.

The first series explores **Srinivasa Ramanujan**. View the [web-based landing page](html/index.html) for a visual overview.

## Srinivasa Ramanujan Series
See [Introduction to Ramanujan](ramanujan/introduction_ramanujan.md) for a biography and links to his contributions.

### Notebooks
1. **Ramanujan’s Pi Series** ([Notebook](ramanujan/01_Ramanujan_Pi.ipynb) | [HTML](html/01_Ramanujan_Pi.html)): Implements the Chudnovsky algorithm with high-precision error analysis.
2. **Partition Function** ([Notebook](ramanujan/02_Partition_Function.ipynb) | [HTML](html/02_Partition_Function.html)): Computes the Hardy-Ramanujan formula, visualizing p(n)’s growth.
3. **Continued Fractions** ([Notebook](ramanujan/03_Continued_Fraction.ipynb) | [HTML](html/03_Continued_Fraction.html)): Evaluates the Rogers-Ramanujan continued fraction.
4. **Tau Function** ([Notebook](ramanujan/04_Tau_Function.ipynb) | [HTML](html/04_Tau_Function.html)): Analyzes τ(n) with q-series plots.
5. **Mock Theta Functions** ([Notebook](ramanujan/05_Mock_Theta_Functions.ipynb) | [HTML](html/05_Mock_Theta_Functions.html)): Implements mock theta series.

## Getting Started
- Clone: `git clone https://github.com/[your-username]/mathematicians.git`
- Install: `pip install -r requirements.txt`
- Run `.ipynb` files in Jupyter, view `.html` files in a browser, or compile with `python scripts/compile_notebooks.py`

## Future Plans
Additional mathematicians (e.g., Gauss, Turing) will be added.

## License
MIT License. The Ramanujan portrait is AI-generated.