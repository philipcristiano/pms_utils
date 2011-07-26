#!/usr/bin/env python

from distribute_setup import use_setuptools
use_setuptools()

import os
from setuptools import setup, find_packages


def read(fname):
    return open(os.path.join(os.path.dirname(__file__), fname)).read()


setup(
    name='pms_utils',
    version='0.1.0',
    description='Utilities for PMS',
    keywords = 'monitoring',
    url='https://github.com/philipcristiano/pms_utils',
    author='Philip Cristiano',
    author_email='pms@philipcristiano.com',
    license='BSD',
    packages=['pms_utils'],
    install_requires=[
        'jsonrequester',
    ],
    test_suite='tests',
    long_description=read('README.rst'),
    zip_safe=True,
    entry_points="""
    [console_scripts]
    pms_watch = pms.watcher:main
    """
)
