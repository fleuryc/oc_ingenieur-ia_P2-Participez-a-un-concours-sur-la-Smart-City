
[![Codacy Badge](https://api.codacy.com/project/badge/Grade/7caff7db990447ec9dc8a7955884948f)](https://app.codacy.com/gh/fleuryc/oc_ingenieur-ia_P2-Participez-a-un-concours-sur-la-Smart-City?utm_source=github.com&utm_medium=referral&utm_content=fleuryc/oc_ingenieur-ia_P2-Participez-a-un-concours-sur-la-Smart-City&utm_campaign=Badge_Grade_Settings)

# Data is for Good challenge : help Paris become a Smart-City !

Repository of OpenClassrooms' [AI Engineer path](https://openclassrooms.com/fr/paths/188-ingenieur-ia), project #2.

Goal : use Jupyter Notebook to analyse Parisian trees open data.

You can see the results here :
- [Presentation](https://fleuryc.github.io/oc_ingenieur-ia_P2-Participez-a-un-concours-sur-la-Smart-City/index.html)
- [HTML page with interactive plots](https://fleuryc.github.io/oc_ingenieur-ia_P2-Participez-a-un-concours-sur-la-Smart-City/main.html)
- [PDF file with static images](https://fleuryc.github.io/oc_ingenieur-ia_P2-Participez-a-un-concours-sur-la-Smart-City/main.pdf)


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

  - If using Jupyter Notebook instead of JupyterLab, uncomment the following lines in the notebook

````python
import plotly.io as pio
pio.renderers.default='notebook'
````
