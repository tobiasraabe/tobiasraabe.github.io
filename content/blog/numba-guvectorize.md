Title: Numba - @vectorize and @guvectorize
Date: 2019-04-14
Tags: Numba, Numpy
Author: Tobias Raabe
Notebook: true

[![Binder](https://mybinder.org/badge.svg)](https://mybinder.org/v2/gh/tobiasraabe/tobiasraabe.github.io/sources?filepath=notebooks%2Fnumba-guvectorize.ipynb)

In this post, I will explain how to use the @vectorize and @guvectorize decorator from Numba. You can use the former if you want to write a function which extrapolates from scalars to elements of arrays and the latter for a function which extrapolates from arrays to arrays of higher dimensions.

<!-- PELICAN_END_SUMMARY -->

{% notebook ../notebooks/numba-guvectorize.ipynb %}
