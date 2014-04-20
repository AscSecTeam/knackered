#!/usr/bin/env python

from setuptools import setup, find_packages

from knackered import __author__, __version__

setup(
    name="knackered",
    version=__version__,
    author=__author__,
    author_email="ascsecteam@live.com",
    packages=find_packages(),
    install_requires=["docopt==0.6.1"],
    description="A network competition scoring engine",
    license="MIT",
    url='https://github.com/AscSecTeam/knackered',
    classifiers=[
        "Intended Audience :: Developers",
        "Programming Language :: Python",
        "Programming Language :: Python :: 2.7",
        "License :: OSI Approved :: MIT License",
    ],
)
