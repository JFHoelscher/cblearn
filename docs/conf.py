# Configuration file for the Sphinx documentation builder.
#
# This file only contains a selection of the most common options. For a full
# list see the documentation:
# https://www.sphinx-doc.org/en/master/usage/configuration.html

# -- Path setup --------------------------------------------------------------

# If extensions (or references to document with autodoc) are in another directory,
# add these directories to sys.path here. If the directory is relative to the
# documentation root, use os.path.abspath to make it absolute, like shown here.
#
import os
import sys
sys.path.insert(0, os.path.abspath('..'))


# -- Project information -----------------------------------------------------

project = 'cblearn'
author = 'David-Elias Künstle, Leena Suresh, Siyavash Haghiri, Michael Perrot, Debarghya Ghoshdastidari, Ulrike von Luxburg'
copyright = f'2021, {author}'

# -- General configuration ---------------------------------------------------

# Add any Sphinx extension module names here, as strings. They can be
# extensions coming with Sphinx (named 'sphinx.ext.*') or your custom
# ones.
extensions = [
    'sphinx.ext.autodoc',
    'sphinx.ext.autodoc.typehints',
    'sphinx.ext.autosummary',
    'sphinx.ext.intersphinx',
    'sphinx.ext.viewcode',
    'sphinx.ext.mathjax',
    'sphinx.ext.napoleon',
    'sphinx_rtd_theme',
    'sphinx_gallery.gen_gallery',
]

autosummary_generate = True  # generate stub files for summarized entries
autodoc_default_options = {
    'members': True,
    'inherited-members': True,
    'class-doc-from': 'class',
}
autodoc_typehints = 'description'
autodoc_typehints_description_target = 'documented'

sphinx_gallery_conf = {
     'examples_dirs': '../examples',   # path to your example scripts
     #'filename_pattern': r'.\.py',
     'gallery_dirs': 'generated_examples',  # path to where to save gallery generated output
}

intersphinx_mapping = {
    'python': ('https://docs.python.org/{.major}'.format(sys.version_info), None),
    'numpy': ('https://docs.scipy.org/doc/numpy/', None),
    'scipy': ('https://docs.scipy.org/doc/scipy/reference', None),
    'matplotlib': ('https://matplotlib.org/', None),
    'pandas': ('https://pandas.pydata.org/pandas-docs/stable/', None),
    'joblib': ('https://joblib.readthedocs.io/en/latest/', None),
    'seaborn': ('https://seaborn.pydata.org/', None),
}

# Add any paths that contain templates here, relative to this directory.
templates_path = ['_templates']

# List of patterns, relative to source directory, that match files and
# directories to ignore when looking for source files.
# This pattern also affects html_static_path and html_extra_path.
exclude_patterns = ['_build', 'Thumbs.db', '.DS_Store']

rst_prolog = """.. attention::
    cblearn is work in progress. The API is still changing and a errors are known. Please help us by posting an issue on Github.
"""

# -- Options for HTML output -------------------------------------------------

# The theme to use for HTML and HTML Help pages.  See the documentation for
# a list of builtin themes.
#
html_theme = 'sphinx_rtd_theme'

# Add any paths that contain custom static files (such as style sheets) here,
# relative to this directory. They are copied after the builtin static files,
# so a file named "default.css" will overwrite the builtin "default.css".
html_static_path = ['_static']
