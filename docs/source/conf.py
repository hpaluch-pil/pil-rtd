# Configuration file for the Sphinx documentation builder.
#
# This file only contains a selection of the most common options. For a full
# list see the documentation:
# http://www.sphinx-doc.org/en/master/config

# -- Path setup --------------------------------------------------------------

# If extensions (or modules to document with autodoc) are in another directory,
# add these directories to sys.path here. If the directory is relative to the
# documentation root, use os.path.abspath to make it absolute, like shown here.
#
# import os
# import sys
# sys.path.insert(0, os.path.abspath('.'))

# use rtd_theme - from: https://github.com/python-pillow/Pillow
import sphinx_rtd_theme

# -- Project information -----------------------------------------------------

project = 'Pickering Interfaces Ltd on Read the Docs'
copyright = '2019, Pickering Interfaces Ltd'
author = 'Henryk Paluch of PIL'

# The full version, including alpha/beta/rc tags
release = '0.9'


# -- General configuration ---------------------------------------------------

# Add any Sphinx extension module names here, as strings. They can be
# extensions coming with Sphinx (named 'sphinx.ext.*') or your custom
# ones.
extensions = [
]

# Add any paths that contain templates here, relative to this directory.
templates_path = ['_templates']

# List of patterns, relative to source directory, that match files and
# directories to ignore when looking for source files.
# This pattern also affects html_static_path and html_extra_path.
exclude_patterns = ['*~','*.swp']


# -- Options for HTML output -------------------------------------------------

# The theme to use for HTML and HTML Help pages.  See the documentation for
# a list of builtin themes.
#
html_theme = "sphinx_rtd_theme"
html_theme_path = [sphinx_rtd_theme.get_html_theme_path()]

# Add any paths that contain custom static files (such as style sheets) here,
# relative to this directory. They are copied after the builtin static files,
# so a file named "default.css" will overwrite the builtin "default.css".
html_static_path = ['_static']

html_logo =  '_static/images/pil-logo.png'


# Changed in Sphinx 2.0, needed in 1.x on Debian
# see: http://www.sphinx-doc.org/en/master/usage/configuration.html
master_doc = 'index'

# render build time at the bottom of page
# see: https://stackoverflow.com/a/51295617
html_last_updated_fmt = '%b %d, %Y %H:%M:%S'

# from: https://github.com/sphinx-gallery/sphinx-gallery/blob/master/doc/conf.py
def setup(app):
    app.add_stylesheet('theme_override.css')

