# ---
# jupyter:
#   jupytext:
#     text_representation:
#       extension: .py
#       format_name: light
#       format_version: '1.5'
#       jupytext_version: 1.14.1
#   kernelspec:
#     display_name: Python 3 (ipykernel)
#     language: python
#     name: python3
# ---

# # Programming in Python
# ## Exam: January 25, 2023
#
# You can solve the exercises below by using standard Python 3.10 libraries, NumPy, Matplotlib, Pandas, PyMC3.
# You can browse the documentation: [Python](https://docs.python.org/3.10/), [NumPy](https://numpy.org/doc/stable/user/index.html), [Matplotlib](https://matplotlib.org/stable/users/index.html), [Pandas](https://pandas.pydata.org/pandas-docs/stable/user_guide/index.html), [PyMC3](https://docs.pymc.io/en/v3/index.html).
# You can also look at the [slides of the course](https://homes.di.unimi.it/monga/lucidi2223/pyqb00.pdf) or your code on [GitHub](https://github.com).
#
# **It is forbidden to communicate with others.**
#
#
#
#

import numpy as np
import pandas as pd  # type: ignore
import matplotlib.pyplot as plt # type: ignore
import pymc as pm   # type: ignore
import arviz as az   # type: ignore

# ### Exercise 1 (max 3 points)
#
# The file [pigs.csv](./pigs.csv) (Koen, Erin, Newton, Erica, & Ellington, E. Hance. (2022). Data for: Evaluating potential sources of invasive wild pigs in Ontario. https://doi.org/10.5061/dryad.5dv41ns6j) contains data about a population of pigs.
#
# The columns have this meaning:
#
#  - PigType - type of pig sighting (domesticated, wild boar, unknown)
#  - DETECTED - 0 - random location, 1 - pig sighting
#  - dist_boar - distance (meters) to nearest known premise with wild boar (meters)
#  - dist_pig - distance (meters) to nearest known premise with domestic pig (meters)
#  - borderMI - distance (meters) to border with Michigan (excluding the upper peninsula)
#  - borderNY - distance (meters) to border with New York (meters)
#  - borderQC - distance (meters) to border with Quebec
#
#
# Load the data in a pandas dataframe and make a `bool` column `pig_sighting` which is `True` iff the pig was detected from a pig sighting site. Use the first column as index.

pass

# ### Exercise 2 (max 4 points)
#
# Make a figure with the three histograms of the distances from the borders. Add a proper title and a legend.
#

pass

# ### Exercise 3 (max 7 points)
#
# Define a function `area` that takes the length of three radii (in **meters**) and computes the area (in square **kilometers**) of the circle with the maximum radius. For example if the three radii are 1000.0, 2000.0, and 3000.0 meters long, the area is  $9\pi$ square kilometers.
#
# To get the full marks, you should declare correctly the type hints and add a test within a doctest string.

pass

# ### Exercise 4 (max 4 points)
#
# Add a column to the data with the `area` computed in the previous exercise, where the three radius are the distances from the border of Michigan, New York, and Quebec.
#
# To get the full marks avoid the use of explicit loops.

pass

# ### Exercise 5 (max 4 points)
#
# Print the mean `dist_boar` and the mean `dist_pig` for wild boars and domesticated detected in pig sighting sites. All domesticated (pot bellied or not) pigs should be considered together.

pass

# ### Exercise 6 (max 3 points)
#
# Make a scatter plot of `dist_boar` vs. `dist_pig`. Pigs detected in a pig sighting site should appear in red, the others in blue.

pass

# ### Exercise 7 (max 3 points)
#
# Sample 5 pigs among the "wild boars" and print, in ascending order of `dist_pig`, their `borderMI`.  

pass

# ### Exercise 8 (max 5 points)
#
# Consider this statistical model:
#
#
# - the `borderQC` distance for wild boars is normally distributed with mean $\mu$ and standard deviation $\sigma$
# - $\mu$ is normally distributed with mean $=170000$ and standard deviation $=100000$
# - $\sigma$ is exponentially distributed with $\lambda = 1$
#
# Code this model with pymc, sample the model, and print the summary of the resulting estimation by using `az.summary`.
#
#
#
#


pass
