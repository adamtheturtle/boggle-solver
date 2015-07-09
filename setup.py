#!/usr/bin/env python

from setuptools import setup, find_packages
import os.path

description = open(
    os.path.join(os.path.dirname(__file__), 'README.md'), 'rb').read()


setup(
    name="bogglesolver",
    version="1.0.0",
    description="Solve a game of Boggle.",
    long_description=description,
    author="Adam Dangoor",
    author_email="adamdangoor@gmail.com",
    install_requires=[],
    zip_safe=True,
    packages=find_packages('.'),
    classifiers=[
        'Intended Audience :: Developers',
        'License :: OSI Approved :: MIT Software License',
        'Operating System :: OS Independent',
        'Programming Language :: Python',
        ],
)
