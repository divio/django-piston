#!/usr/bin/env python
# -*- coding: utf-8 -*-
from setuptools import setup, find_packages

from piston import __version__



setup(
    name = "django-piston",
    version = __version__,
    url = 'http://bitbucket.org/jespern/django-piston/wiki/Home',
	download_url = 'http://bitbucket.org/jespern/django-piston/downloads/',
    license = 'BSD',
    description = "Piston is a Django mini-framework creating APIs.",
    author = 'Jesper Noehr',
    author_email = 'jesper@noehr.org',
    packages = find_packages(),
    include_package_data = True,
    zip_safe = False,
    classifiers = [
        'Development Status :: 3 - Alpha',
        'Framework :: Django',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: BSD License',
        'Operating System :: OS Independent',
        'Programming Language :: Python',
        'Topic :: Internet :: WWW/HTTP',
    ]
)
