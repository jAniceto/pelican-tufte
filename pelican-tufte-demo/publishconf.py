# This file is only used if you use `make publish` or
# explicitly specify it as your config file.

import os
import sys
sys.path.append(os.curdir)
from pelicanconf import *

# If your site is available via HTTPS, make sure SITEURL begins with https://
SITEURL = 'https://janiceto.github.io/pelican-tufte'
RELATIVE_URLS = False

FEED_ALL_ATOM = 'feeds/all.atom.xml'
CATEGORY_FEED_ATOM = 'feeds/{slug}.atom.xml'

DELETE_OUTPUT_DIRECTORY = True

# Following items are often useful when publishing

#DISQUS_SITENAME = ""
#GOOGLE_ANALYTICS = ""

MENUITEMS = (
    ('Bio', f'{SITEURL}'),
    ('Publications', f'{SITEURL}/category/publications.html'),
    ('Teaching', f'{SITEURL}/category/teaching.html'),
    ('Talks', f'{SITEURL}/category/talks.html'),
    ('Projects', f'{SITEURL}/category/projects.html'),
    ('Blog', f'{SITEURL}/blog.html'),
    ('Contact', f'{SITEURL}/pages/contact.html'),
)