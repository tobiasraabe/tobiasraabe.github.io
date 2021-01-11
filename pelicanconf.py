from pelican_jupyter import liquid as nb_liquid

# Pelican options
LOAD_CONTENT_CACHE = False

# General
AUTHOR = "Tobias Raabe"
SITEURL = "https://tobiasraabe.github.io"
SITENAME = "Tobias Raabe's Blog"
SITETITLE = "Tobias Raabe"
SITESUBTITLE = ""
SITEDESCRIPTION = ""
SITELOGO = "/extra/avatar.png"
FAVICON = ""

BROWSER_COLOR = "#333"
ROBOTS = "index, follow"

CC_LICENSE = {
    "name": "Creative Commons Attribution-ShareAlike",
    "version": "4.0",
    "slug": "by-sa"
}

COPYRIGHT_YEAR = 2021

RELATIVE_URLS = True

PATH = "content"
PAGE_PATHS = ["pages"]
PAGE_URL = "{slug}.html"
PAGE_SAVE_AS = "{slug}.html"
ARTICLE_PATHS = ["Blog"]
ARTICLE_URL = "blog/{slug}.html"
ARTICLE_SAVE_AS = "blog/{slug}.html"
ARCHIVES_SAVE_AS = "archives.html"

MENUITEMS = [
    ("Archives", "/archives.html"),
    ("Categories", "/categories.html"),
    ("Tags", "/tags.html"),
]

DISPLAY_PAGES_ON_MENU = False
LINKS = [
    ("Projects", "/projects.html"),
    ("Publications", "/publications.html"),
    ("CV", "../pdfs/cv.pdf"),
]

DIRECT_TEMPLATES = ["index", "categories", "tags", "archives", "search"]
THEME_TEMPLATES_OVERRIDES = ["templates"]

TIMEZONE = "Europe/Paris"
DEFAULT_LANG = "en"
LOCALE = ("en", "en_US.utf8")

# Feed generation is usually not desired when developing
FEED_ALL_ATOM = None
CATEGORY_FEED_ATOM = None
TRANSLATION_FEED_ATOM = None
AUTHOR_FEED_ATOM = None
AUTHOR_FEED_RSS = None

# Social widget
SOCIAL = (
    ("github", "https://github.com/tobiasraabe"),
    # (
    #     "stackoverflow",
    #     "https://stackoverflow.com/users/7523785/tobiasraabe",
    # ),
    ("linkedin", "https://linkedin.com/in/tobiasraabe"),
    # (
    #     "diploma",
    #     "https://scholar.google.de/citations?user=4MurkHQAAAAJ&hl",
    # ),
    ("twitter", "https://twitter.com/tobraab")
)

THEME = "theme"

CUSTOM_CSS = "static/css/custom.css"
CUSTOM_JS = "static/js/custom.js"

PYGMENTS_STYLE = "default"

MAIN_MENU = True

JINJA_ENVIRONMENT = {"extensions": ["jinja2.ext.i18n"]}
I18N_TEMPLATES_LANG = "en"

PLUGIN_PATHS = ["plugins"]
PLUGINS = [
    "cite",
    "readtime",
    "render_math",
    "summary",
    "tag_cloud",
    "tipue_search",
    "i18n_subsites",
    nb_liquid,
]

# Set article info
SHOW_ARTICLE_AUTHOR = False  # Website with one author
SHOW_ARTICLE_CATEGORY = True
SHOW_DATE_MODIFIED = True

STATIC_PATHS = ["extra", "images", "pdfs"]

# summary and clean_summary
SUMMARY_MAX_LENGTH = 150
SUMMARY_USE_FIRST_PARAGRAPH = False
CLEAN_SUMMARY_MAXIMUM = 1

# pelican-ipynb
IGNORE_FILES = [".ipynb_checkpoints", "*.bib.bak", "*.bib.sav"]
# IPYNB_FIX_CSS = True
IPYNB_SKIP_CSS = True
MARKUP = ("md",)
LIQUID_CONFIGS = [("IPYNB_EXPORT_TEMPLATE", "notebook.tpl", "")]

# readtime for articles
SHOW_READTIME = True

# cite
PUBLICATIONS_SRC = "content/references.bib"


# Analytics
GOOGLE_ANALYTICS = "UA-178274443-1"
