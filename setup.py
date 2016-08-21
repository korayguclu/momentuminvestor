# -*- coding: utf-8 -*-

from distutils.core import setup
from setuptools import find_packages

setup(
    name='momentuminvestor',
    version='0.1.0',
    author='Koray Guclu',
    author_email='korayguclu@gmail.com',
    license='LICENSE',
    description='momentuminvestor is a Python package which allows you to build predefined momentum dashboard.',
    url='https://github.com/korayguclu/momentuminvestor',
    install_requires=[line.strip("\n") for line in open("requirements.txt", "r").readlines()],
    include_package_data=True,
    packages=find_packages(),
)