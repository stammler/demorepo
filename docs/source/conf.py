# Configuration file for the Sphinx documentation builder.

# -- Project information

project = 'Calculator'
copyright = '2024, Sebastian Stammler'
author = 'Sebastian Stammler'

# -- General configuration

extensions = [
    'nbsphinx',
    'sphinx.ext.autodoc',
    'sphinx.ext.autosummary',
    'sphinx.ext.duration',
    'sphinx.ext.napoleon',
    'sphinx.ext.viewcode',
    'sphinx_automodapi.automodapi',
]

# -- Options for HTML output

html_theme = 'sphinx_rtd_theme'

# -- Options for EPUB output
epub_show_urls = 'footnote'
