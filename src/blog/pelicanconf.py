#!/usr/bin/env python
# -*- coding: utf-8 -*- #
from __future__ import unicode_literals

AUTHOR = "Simon Weiss"
SITENAME = "Simon says"
SITEURL = "https://simoncw.github.io"
SITELOGO = "images/profile/simoncw_profile.jpg"
SITETITLE = "Simon says"
SITESUBTITLE = "Musings on my work as a full-stack data scientist"
PATH = "content"


STATIC_PATHS = ["images"]

TIMEZONE = "Europe/Paris"

DEFAULT_LANG = "en"

THEME = "/home/simon/repos/other/themes/Flex"

# Feed generation is usually not desired when developing
FEED_ALL_ATOM = 'feeds/all.atom.xml'
FEED_ALL_RSS = 'feeds/all.rss.xml'
AUTHOR_FEED_RSS = 'feeds/{slug}.rss.xml'
RSS_FEED_SUMMARY_ONLY = False

# Blogroll
#LINKS = (("Pelican", "http://getpelican.com/"),
#         ("Python.org", "http://python.org/"),
#         ("Jinja2", "http://jinja.pocoo.org/"))


DEFAULT_PAGINATION = 10

# Uncomment following line if you want document-relative URLs when developing
#RELATIVE_URLS = True


SOCIAL = (
    ("linkedin", "https://linkedin.com/in/weiss-simon"),
    ("twitter", "https://twitter.com/SimonCWeiss"),
    ("github", "https://github.com/SimonCW"),
    ("stack-overflow", "https://stackoverflow.com/users/6663432/simoncw"),
)