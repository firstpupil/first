#! /usr/bin/env python
# -*- coding: utf-8 -*-

from sys import argv, exit
import os, re

if "upl" in argv[1:]:
    os.system("python setup.py register -r pypi")
    os.system("python setup.py sdist upload -r pypi")
    exit()

m = open(os.path.join(os.path.dirname(os.path.abspath(__file__)), "firstctrl", "_version.py")).read()
version = re.findall(r"__version__ *= *\"(.*?)\"", m)[0]

try:
    from setuptools import setup
    setup
except ImportError:
    from distutils.core import setup
    setup

setup(
    name = "firstctrl",
    version = version,
    author = "Guillaume Schworer",
    author_email = "guillaume.schworer@gmail.com",
    packages = ["firstctrl"],
    url = "https://github.com/firstpupil/firstctrl/",
    license = "GNU General Public License v3 or later (GPLv3+)",
    description = "Pupil remapping control software",
    long_description = open("README.rst").read() + "\n\n"
                    + "Changelog\n"
                    + "---------\n\n"
                    + open("HISTORY.rst").read(),
    package_data = {"": ["LICENSE", "AUTHORS.rst", "HISTORY.rst", "README.rst"]},
    include_package_data = True,
    install_requires = [],
    download_url = 'https://github.com/firstpupil/firstctrl/tree/master/dist',
    keywords = [],
    classifiers = [
        "Development Status :: 4 - Beta",
        "Environment :: Console",
        "Intended Audience :: Developers",
        'Intended Audience :: Education',
        "Intended Audience :: Science/Research",
        "License :: OSI Approved :: GNU General Public License v3 or later (GPLv3+)",
        "Operating System :: OS Independent",
        "Programming Language :: Python",
        "Topic :: Documentation :: Sphinx",
    ],
)
