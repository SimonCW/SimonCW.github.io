#!/usr/bin/env python
# -*- coding: utf-8 -*- #
from __future__ import unicode_literals

AUTHOR = "Simon Weiss"
SITENAME = "Simon's Landingzone"
SITEURL = "https://simoncw.github.io"
SITELOGO = "images/profile/simoncw_profile.jpg"
PATH = "content"

STATIC_PATHS = ["images"]

TIMEZONE = "Europe/Paris"

DEFAULT_LANG = "en"

THEME = "/home/simon/repos/other/themes/Flex"

# Feed generation is usually not desired when developing
FEED_ALL_ATOM = None
CATEGORY_FEED_ATOM = None
TRANSLATION_FEED_ATOM = None
AUTHOR_FEED_ATOM = None
AUTHOR_FEED_RSS = None

# Blogroll
#LINKS = (("Pelican", "http://getpelican.com/"),
#         ("Python.org", "http://python.org/"),
#         ("Jinja2", "http://jinja.pocoo.org/"))


DEFAULT_PAGINATION = 10

# Uncomment following line if you want document-relative URLs when developing
#RELATIVE_URLS = True


SOCIAL = (
    ("linkedin", "www.linkedin.com/in/weiss-simon"),
    ("twitter", "https://twitter.com/SimonCWeiss"),
    ("github", "https://github.com/SimonCW"),
    ("stack-overflow", "https://stackoverflow.com/users/6663432/simoncw"),
)