# oc_ingenieur-ia_P2-Participez-a-un-concours-sur-la-Smart-City
Repository of OpenClassrooms' AI Engineer path, project #2 : use Jupyter Notebook to analyse some open data

You can see the results here :
- [main.pdf](output/main.pdf)
- [main.html](output/main.html)

## Requirements

- Conda

````bash
# conda install jupyterlab ipywidgets numpy pandas matplotlib seaborn plotly statsmodels
# or :
conda env update -f environment.yml
````

- Pip

```bash
# pip install jupyterlab ipywidgets numpy pandas matplotlib seaborn plotly statsmodels
# or :
pip install -r requirements.txt
```

- Fix Plotly issues with JupyterLab

cf. [Plotly troubleshooting](https://plotly.com/python/troubleshooting/#jupyterlab-problems)

```bash
jupyter labextension install jupyterlab-plotly
```

- If using Jupyter Notebook instead of JupyterLab, uncomment the following lines in the notebook :
````python
import plotly.io as pio
pio.renderers.default='notebook'
````
