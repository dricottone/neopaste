#!/usr/bin/env python3

from setuptools import setup

long_description = None
with open('README.md', encoding='utf-8') as f:
    long_description = f.read()

setup(
    name="neopaste",
    packages=["neopaste"],
    version="1.0.0",
    license="GPL",
    description="Paste file streams side-by-side",
    long_description=long_description,
    long_description_content_type='text/markdown',
    author="Dominic Ricottone",
    author_email="me@dominic-ricottone.com",
    url="git.dominic-ricottone.com/neopaste",
    entry_points={"console_scripts": ["npaste = neopaste.__main__:main"]},
    install_requires=["wcwidth>=0.2.4"],
    python_requires=">=3.6",
)

