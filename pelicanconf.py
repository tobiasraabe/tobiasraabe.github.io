#!/usr/bin/env python
# -*- coding: utf-8 -*- #
from __future__ import unicode_literals

# Pelican options
LOAD_CONTENT_CACHE = False

# General
AUTHOR = 'Tobias Raabe'
SITENAME = 'Tobias Raabe'
SITEURL = ''
RELATIVE_URLS = True

PATH = 'content'
PAGE_PATHS = ['pages']
PAGE_URL = '{slug}.html'
PAGE_SAVE_AS = '{slug}.html'
ARTICLE_PATHS = ['blog']
ARTICLE_URL = 'blog/{slug}.html'
ARTICLE_SAVE_AS = 'blog/{slug}.html'
ARCHIVES_SAVE_AS = 'archives.html'

MENUITEMS = (('Curriculum Vitae', 'static/cv.pdf'),)

DIRECT_TEMPLATES = ['index', 'categories', 'tags', 'archives', 'search']

TIMEZONE = 'Europe/Paris'
DEFAULT_LANG = 'en'
LOCALE = 'en'

# Feed generation is usually not desired when developing
FEED_ALL_ATOM = None
CATEGORY_FEED_ATOM = None
TRANSLATION_FEED_ATOM = None
AUTHOR_FEED_ATOM = None
AUTHOR_FEED_RSS = None

# Social widget
SOCIAL = (
    ('Github', 'https://github.com/tobiasraabe'),
    (
        'Stack Overflow',
        'https://stackoverflow.com/users/7523785/brimborium',
        'stack-overflow',
    ),
    ('linkedin', 'https://linkedin.com/in/tobiasraabe'),
)

DEFAULT_PAGINATION = 50

### Theme related options
THEME = 'theme'
BOOTSTRAP_THEME = 'united'
BOOTSTRAP_FLUID = False
FAVICON = 'extra/favicon.png'
# AVATAR ='extra/gear-wrench-icon-512-278694.png'
CUSTOM_CSS = 'static/css/custom.css'
CUSTOM_JS = 'static/js/custom.js'
PYGMENTS_STYLE = 'default'
USE_PAGER = True
DISPLAY_BREADCRUMBS = True
DISPLAY_CATEGORY_IN_BREADCRUMBS = True
DISPLAY_CATEGORIES_ON_MENU = False
DISPLAY_ARTICLE_INFO_ON_INDEX = False  # Without effect.
JINJA_ENVIRONMENT = {'extensions': ['jinja2.ext.i18n']}
I18N_TEMPLATES_LANG = 'en'

PLUGIN_PATHS = ['plugins']
PLUGINS = [
    'cite',
    'ipynb.liquid',
    'i18n_subsites',
    'toc',
    'readtime',
    'render_math',
    'series',
    'summary',
    'tag_cloud',
    'tipue_search',
]

# Set article info
SHOW_ARTICLE_AUTHOR = False  # Website with one author
SHOW_ARTICLE_CATEGORY = True
SHOW_DATE_MODIFIED = True

STATIC_PATHS = ['static', 'extra']

EXTRA_PATH_METADATA = {
    'extra/custom.css': {'path': 'static/css/custom.css'},
    'extra/custom.js': {'path': 'static/js/custom.js'},
}

# summary and clean_summary
SUMMARY_MAX_LENGTH = 150
SUMMARY_USE_FIRST_PARAGRAPH = True
CLEAN_SUMMARY_MAXIMUM = 1

# pelican-ipynb
IGNORE_FILES = ['.ipynb_checkpoints', '*.bib.bak', '*.bib.sav']
IPYNB_SKIP_CSS = True
MARKUP = ('md',)

# series
SERIES_TEXT = 'Part %(index)s of %(name)s'

# readtime for articles
SHOW_READTIME = True

# toc
TOC = {
    'TOC_HEADERS': '^h[1-6]',
    'TOC_RUN': 'true',
    'TOC_INCLUDE_TITLE': 'false',
    'TOC_PARAGRAPH_SIGN': 'false',
}

# tag_cloud
TAG_CLOUD_BADGE = True
TAG_CLOUD_SORTING = 'alphabetically'
TAG_CLOUD_STEPS = 3

# cite
PUBLICATIONS_SRC = 'content/references.bib'
