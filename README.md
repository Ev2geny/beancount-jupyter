# Header


Open the notebook in JupyterLab (recommended)
https://mybinder.org/v2/gh/Ev2geny/beancount-jupyter/develop?urlpath=lab/tree/beancount-jupyter.ipynb

Open the notebook in Classic Notebook

https://mybinder.org/v2/gh/Ev2geny/beancount-jupyter/develop?urlpath=tree/beancount-jupyter.ipynb



To export HTML with no input
`jupyter nbconvert beancount-jupyter.ipynb --to html --no-input`

To export to HTML with some input hidden
`jupyter nbconvert beancount-jupyter.ipynb --to html -TagRemovePreprocessor.enabled=True --TagRemovePreprocessor.remove_input_tags hide-input`
