AUTHOR = 'Aniceto'
SITENAME = 'Lorem Ipsum'
SITESUBTITLE = 'Lorem ipsum dolor sit amet'
SITEURL = 'http://127.0.0.1:8000'

PATH = 'content'

TIMEZONE = 'GMT'

DEFAULT_LANG = 'EN'

# Feed generation is usually not desired when developing
FEED_ALL_ATOM = None
CATEGORY_FEED_ATOM = None
TRANSLATION_FEED_ATOM = None
AUTHOR_FEED_ATOM = None
AUTHOR_FEED_RSS = None

# Blogroll
LINKS = (
    ('Pelican', 'https://getpelican.com/'),
    ('Python.org', 'https://www.python.org/'),
    ('Jinja2', 'https://palletsprojects.com/p/jinja/'),
)

# Social widget
SOCIAL = (
    ('Scopus', '#'),
    ('ORCID', '#'),
    ('Google Scholar', '#'),
    ('Twitter', '#'),
)

DEFAULT_PAGINATION = False

# Uncomment following line if you want document-relative URLs when developing
#RELATIVE_URLS = True

THEME = 'C:/Users/José Aniceto/Dropbox/Projectos/pelican-tufte/tufte-theme'

PROFILE_IMAGE_URL = 'https://placehold.jp/500x500.png'

# INDEX_SAVE_AS = 'blog_index.html'

DISPLAY_PAGES_ON_MENU = False
DISPLAY_CATEGORIES_ON_MENU = False
MENUITEMS = (
    ('Bio', '/'),
    ('Publications', '/category/publications.html'),
    ('Teaching', '/category/teaching.html'),
    ('Talks', '/category/talks.html'),
    ('Projects', '/category/projects.html'),
    ('Contact', '/pages/contact.html'),
)