# Configuration file for the Sphinx documentation builder.
#
# For the full list of built-in configuration values, see the documentation:
# https://www.sphinx-doc.org/en/master/usage/configuration.html

import os
import sys

# -- Path setup and Versioning -----------------------------------------------
# If not a package, default version is used.
release = "0.0.1"
sys.path.insert(0, os.path.abspath(".."))
sys.path.insert(0, os.path.abspath("./jupyternb"))

# -- Project information -----------------------------------------------------
project = "OnlyPoetry"
author = "Yuji Okano"

# -- General configuration ---------------------------------------------------
extensions = [
    "sphinx.ext.autodoc",
    "sphinx.ext.napoleon",  # NumPy/Google style docstrings
    "sphinx.ext.viewcode",
    "sphinx.ext.mathjax",
    "nbsphinx",  # Jupyter Notebook support
    "sphinx_gallery.load_style",
    "myst_parser",  # Markdown support
]

templates_path = ["_templates"]
exclude_patterns = ["_build", "Thumbs.db", ".DS_Store", "**.ipynb_checkpoints"]

source_suffix = {
    ".rst": "restructuredtext",
    ".md": "markdown",
}

# -- Options for Autodoc & Napoleon ------------------------------------------
autodoc_member_order = "bysource"
autodoc_typehints = "description"
napoleon_google_docstring = False
napoleon_numpy_docstring = True
napoleon_include_init_with_doc = True

# -- Options for HTML output -------------------------------------------------
html_theme = "sphinx_rtd_theme"
html_static_path = ["_static"]
html_logo = "_static/default_logo.png"

html_theme_options = {
    "navigation_depth": 5,
    "logo_only": True,
}

htmlhelp_basename = "basalcelldemo-onlypoetry"
# html_extra_path = ["r_api"]
# -- Options for LaTeX output ------------------------------------------------
latex_documents = [
    ("index", "onlypoetry.tex", "OnlyPoetry Analysis Details", author, "manual"),
]

# -- Options for manual page output ------------------------------------------
man_pages = [("index", "onlypoetry", "OnlyPoetry Analysis Details", [author], 1)]

# -- Options for Texinfo output ----------------------------------------------
texinfo_documents = [
    (
        "index",
        "onlypoetry",
        "OnlyPoetry Analysis Details",
        author,
        "onlypoetry",
        "Reproducibility control for BasalCellDemo "
        "using a Poetry-only Python environment",
        "Miscellaneous",
    ),
]

# -- Options for nbsphinx -----------------------------------------
nbsphinx_execute = "never"
nbsphinx_allow_errors = False

# nbsphinx_thumbnails = {
#     # assign your nbsphinx gallery thumbnails if you need them
#     # e.g,)
#     # "jupyternb/ipynb_name_without_file_extension": "_static/custum_thumbnail.png",
# }
