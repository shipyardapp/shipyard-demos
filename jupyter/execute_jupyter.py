import nbformat
from nbconvert.preprocessors import ExecutePreprocessor

with open('jupyter_demo.ipynb') as file:
    notebook = nbformat.read(file, as_version=4)

processor = ExecutePreprocessor(timeout=600, kernel_name='python3')

processor.preprocess(notebook)

with open('executed_notebook.ipynb', 'w', encoding='utf-8') as file:
    nbformat.write(notebook, file)
