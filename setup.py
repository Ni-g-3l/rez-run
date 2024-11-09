from __future__ import print_function, with_statement
from setuptools import setup, find_packages


setup(
    name="rez_run",
    version="0.1.0",
    package_dir={
        "rez_run": "rez_run"
    },
    packages=find_packages(where="."),
)
