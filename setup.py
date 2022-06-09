# coding: utf-8

"""
    TzKT API
    OpenAPI spec version: v1.8.3
    Contact: hello@baking-bad.org
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""
from os import path
from setuptools import setup, find_packages  # noqa: H301

NAME = "tzktpy"
VERSION = "1.0.0"
# To install the library, run the following
#
# python setup.py install
#
# prerequisite: setuptools
# http://pypi.python.org/pypi/setuptools

REQUIRES = ["urllib3 >= 1.15", "six >= 1.10", "certifi", "python-dateutil"]

this_directory = path.abspath(path.dirname(__file__))
with open(path.join(this_directory, "README.md"), encoding="utf-8") as f:
    long_description = f.read()

setup(
    name=NAME,
    version=VERSION,
    description="TzKT API",
    author_email="hello@baking-bad.org",
    url="",
    keywords=["Swagger", "TzKT API"],
    install_requires=REQUIRES,
    packages=find_packages(),
    include_package_data=True,
    long_description=long_description
)
