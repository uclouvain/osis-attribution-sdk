# coding: utf-8

"""
    Attribution Service

    A set of API endpoints that allow you to get information about attribution  # noqa: E501

    The version of the OpenAPI document: 1.00
    Generated by: https://openapi-generator.tech
"""


from setuptools import setup, find_packages  # noqa: H301

NAME = "osis-attribution-sdk"
VERSION = "1.0.0"
# To install the library, run the following
#
# python setup.py install
#
# prerequisite: setuptools
# http://pypi.python.org/pypi/setuptools

REQUIRES = ["urllib3 >= 1.25.3", "six >= 1.10", "python-dateutil"]

setup(
    name=NAME,
    version=VERSION,
    description="Attribution Service",
    author="OpenAPI Generator community",
    author_email="team@openapitools.org",
    url="",
    keywords=["OpenAPI", "OpenAPI-Generator", "Attribution Service"],
    install_requires=REQUIRES,
    packages=find_packages(exclude=["test", "tests"]),
    include_package_data=True,
    long_description="""\
    A set of API endpoints that allow you to get information about attribution  # noqa: E501
    """
)
