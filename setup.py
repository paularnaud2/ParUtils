from setuptools import setup
from setuptools import find_packages

pkg_list = find_packages(exclude=['tests'])
setup(
    packages=pkg_list,
)
