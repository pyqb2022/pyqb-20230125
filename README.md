# Analyze wild pigs data

Data source:

Koen, Erin, Newton, Erica, & Ellington, E. Hance. (2022). Data for: Evaluating
potential sources of invasive wild pigs in Ontario [Data set].
https://doi.org/10.5061/dryad.5dv41ns6j



## Setup

The `exam.py` is intended to be modified as a
[jupyter](https://jupyter.org/) notebook. The notebook format `.ipynb`, however,
is not very convenient for configuration management, testing, and giving
feedback via the usual "pull-request" mechanism provided by Github. Thus, this
repository uses
[jupytext](https://jupytext.readthedocs.io/en/latest/install.html) to **pair** a
pure Python file with a notebook with the same name. The notebook is
automatically created when you open the Python file with jupyter, and the two
files are kept in sync. Do not add `exercise.ipynb` to the files managed by git.

To start, you need the following actions:

```sh
python -m venv VIRTUAL_ENVIRONMENT
# remember to activate the virtual environment according to your operating system rules
pip install -r requirements.txt
jupyter notebook
```

Then you can open the `exam.py` as a notebook in the browser.


## Test

You can execute tests locally on the python file:


```sh
mypy exam.py
python -m doctest exam.py
```
