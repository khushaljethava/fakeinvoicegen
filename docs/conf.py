# Configuration file for the Sphinx documentation builder.
project = 'FakeInvoiceGen'
copyright = '2024, Khushal Jethava'
author = 'Khushal Jethava'
release = '0.1.0'

extensions = [
    'sphinx.ext.autodoc',
    'sphinx.ext.napoleon',
    'sphinx.ext.viewcode',
]

templates_path = ['_templates']
exclude_patterns = ['_build', 'Thumbs.db', '.DS_Store']

html_theme = 'sphinx_rtd_theme'