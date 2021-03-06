# Configuration file for the Sphinx documentation builder.
#
# This file only contains a selection of the most common options. For a full
# list see the documentation:
# https://www.sphinx-doc.org/en/master/usage/configuration.html

# -- Path setup --------------------------------------------------------------

# If extensions (or modules to document with autodoc) are in another directory,
# add these directories to sys.path here. If the directory is relative to the
# documentation root, use os.path.abspath to make it absolute, like shown here.
#
# import os
# import sys
# sys.path.insert(0, os.path.abspath('.'))


# -- Project information -----------------------------------------------------

project = '信号与系统'
author = 'X. Zhao'
copyright = 'CC BY-NC-SA 4.0'

# The full version, including alpha/beta/rc tags
release = '0.5.0'


# -- General configuration ---------------------------------------------------

# If set to a major.minor version string like '1.1', Sphinx will
# compare it with its version and refuse to build if it is too old.
# Default is no requirement.
needs_sphinx = '4.3'

# If true, Sphinx will warn about all references where the target
# cannot be found. Default is False. You can activate this mode
# temporarily using the `-n` command-line switch.
nitpicky = True

language = 'zh_CN'

# Add any Sphinx extension module names here, as strings. They can be
# extensions coming with Sphinx (named 'sphinx.ext.*') or your custom
# ones.
extensions = [
    'myst_parser',
    'numpydoc',
    'sphinx_copybutton',
    'sphinx.ext.githubpages',
    'nbsphinx',
    'IPython.sphinxext.ipython_console_highlighting',
]

# MyST parser configuration
myst_enable_extensions = ['dollarmath']
myst_dmath_allow_labels = True

# MathJax configuration
mathjax_path = 'https://unpkg.com/mathjax@3/es5/tex-mml-chtml.js'

# nbsphinx configuration
nbsphinx_execute = 'never'

def setup(app):
    app.add_js_file('https://unpkg.com/mermaid/dist/mermaid.min.js', priority=499)
    app.add_js_file(None, body='mermaid.initialize({startOnLoad:true, theme:"base"})', priority=499)

# numpydoc config
numpydoc_use_plots = True
numpydoc_validation_checks = {'all'}

# Add any paths that contain templates here, relative to this directory.
templates_path = ['templates']

# List of patterns, relative to source directory, that match files and
# directories to ignore when looking for source files.
# This pattern also affects html_static_path and html_extra_path.
exclude_patterns = []


# -- Options for HTML output -------------------------------------------------

# The theme to use for HTML and HTML Help pages.  See the documentation for
# a list of builtin themes.
#
html_theme = 'pydata_sphinx_theme'
html_logo = 'static/sinusoid.svg'
html_favicon = 'static/sinusoid.ico'
html_theme_options = {
    'navbar_start': ['navbar-brand'],
    'external_links': [
        {
            'name': 'EM Journey',
            'url': 'https://gitee.com/kai-lu/EM_Journey',
        },
        {
            'name': 'EM Journey (GitHub)',
            'url': 'https://github.com/Antenna-Genesis/EM_Journey',
        }
    ],
    'github_url': 'https://github.com/atlanswer/signals-and-systems',
    'use_edit_page_button': True,
    'search_bar_text': '搜索',
    'show_toc_level': 2,
}
html_context = {
    'github_user': 'atlanswer',
    'github_repo': 'signals-and-systems',
    'github_version': 'main',
    'doc_path': 'doc',
}

# Add any paths that contain custom static files (such as style sheets) here,
# relative to this directory. They are copied after the builtin static files,
# so a file named "default.css" will overwrite the builtin "default.css".
html_static_path = ['static']
