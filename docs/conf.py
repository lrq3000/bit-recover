# -*- coding: utf-8 -*-

import sys
import os

sys.path.insert(0, os.path.abspath(''))

extensions = [
    'sphinx.ext.autodoc',
    'sphinx.ext.doctest',
    'sphinx.ext.todo',
    'sphinx.ext.coverage',
    'sphinx.ext.mathjax',
    'sphinx.ext.ifconfig',
    'sphinx.ext.viewcode',
    'sphinx.ext.intersphinx',
]

intersphinx_mapping = {'python': ('http://docs.python.org/3.3', None)}

templates_path = ['_templates']
source_suffix = '.rst'
master_doc = 'index'
project = u'Bit Recovery'
copyright = u'2013, Dirk Roorda'
version = '1.2'
release = '1.2.2'
exclude_patterns = ['_build']
add_function_parentheses = True
add_module_names = False
pygments_style = 'sphinx'
autoclass_content = 'both'

# -- Options for HTML output ----------------------------------------------

on_rtd = os.environ.get('READTHEDOCS', None) == 'True'
if on_rtd:
    html_theme = 'default'
else:
    html_theme = 'sphinx_rtd_theme'
html_theme_path = ["_themes", ]

html_static_path = ['_static']
html_domain_indices = True
html_use_index = True
html_split_index = False
html_show_sourcelink = True
html_show_sphinx = True
html_show_copyright = True
htmlhelp_basename = 'Bit Recovery'

# -- Options for LaTeX output ---------------------------------------------

latex_elements = {
'papersize': 'a4paper',
'pointsize': '10pt',
}

latex_documents = [
  ('index', 'Bit_Recovery.tex', u'Bit Recovery Documentation',
   u'Dirk Roorda', 'manual'),
]

# -- Options for manual page output ---------------------------------------

man_pages = [
    ('index', 'Bit_Recovery', u'Bit Recovery Documentation',
     [u'Dirk Roorda'], 1)
]

# -- Options for Texinfo output -------------------------------------------

texinfo_documents = [
  ('index', 'Bit_Recovery', u'Bit Recovery Documentation',
   u'Dirk Roorda', 'Bit Recovery', 'One line description of project_name.',
   'Miscellaneous'),
]

# -- Options for Epub output ----------------------------------------------

epub_title = u'Bit Recovery'
epub_author = u'Dirk Roorda'
epub_publisher = u'Dirk Roorda'
epub_copyright = u'2013, Dirk Roorda'
epub_basename = u'Bit_Recovery'
epub_theme = 'epub'
epub_show_urls = 'footnote'
epub_use_index = True
