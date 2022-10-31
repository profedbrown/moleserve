"""A setuptools based setup module for A3 project.
   Based on <http://setuptools.readthedocs.io/en/latest/setuptools.html>
"""

from setuptools import setup

setup(
    name="moleflask",
    version="0.1",
    packages=['moleflask'],

    # Check that a package for install is available from PyPI
    install_requires=['flask>=1.0.2'], # PyPI package

    package_data={
        # If any package contains *.txt or *.pdf files, include them:
        '': ['*.txt', '*.pdf'],
        # And everything in the test, doc, static and jinja folders:
        'moleflask': ['docs/*','tests/*', 'static/*', 'templates/*'],
    },

    # metadata for upload to PyPI
    author="Ed Brown",
    author_email="brown@mun.ca",
    description="This is an Example Package, MoleFLask, for COMP2005",
    long_description="README is sometimes put here",
    license="COMP2005 students", # this is incorrect usage
    keywords="flask examples",
    url="http://www.cs.mun.ca/~brown/2005",   # project home page, if any

    # could also include project_urls, long_description, download_url, classifiers, etc.

    # setup_requires=['pytest-runner',], # suggested from flaskr tutorial - but not needed
    # tests_require=['pytest',], # suggested from flaskr tutorial - but not needed
)
