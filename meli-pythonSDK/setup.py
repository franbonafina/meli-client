#!/usr/bin/env python

import os

try:
    from setuptools import setup
except ImportError:
    from distutils.core import setup

version = '1.0'

classifiers = [
    "Development Status :: ..progress",
    "Programming Language :: Python"
]

root_dir = os.path.dirname(__file__)
if not root_dir:
    root_dir = '.'

setup(
    name='meli-python-sdk',
    version=version,    
    author='Franco Bonafina',
    author_email='franbonafina1@gmail.com',
    license='The MIT License',
    packages=['melipy'],
    install_requires=[
        'requests'
    ],
    py_modules=['core', 'meliresources'],
    description='Mercado Libre Python SDK',
    classifiers=classifiers,
    keywords='Mercado Libre SDK',
)
