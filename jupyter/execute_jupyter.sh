pip install jupyter

python --version
jupyter --version

jupyter nbconvert --to html --ExecutePreprocessor.timeout=600 --execute jupyter_demo.ipynb 