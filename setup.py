# -*- coding: utf-8 -*-

import os

from setuptools import (
    setup,
    find_packages,
)

here = os.path.dirname(__file__)
requires = [
    'redis',
]
tests_require = [
    'nose',
    'coverage',
    'mock',
]


def _read(name):
    try:
        return open(os.path.join(here, name)).read()
    except:
        return ""
readme = _read("README.rst")
license = _read("LICENSE.rst")

setup(
    name='redisengine',
    version='0.0.1',
    test_suite='redisengine',
    author='Kohei YOSHIDA',
    author_email='license@yosida95.com',
    description='a ORM for Redis.',
    long_description=readme,
    license=license,
    url='https://github.com/yosida95/redisengine',
    packages=find_packages(),
    install_requires=requires,
    tests_require=tests_require,
    classifiers=[
        "Development Status :: 2 - Pre-Alpha",
        "Intended Audience :: Developers",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
        "Programming Language :: Python",
        "Programming Language :: Python :: 2.7",
        "Topic :: Internet :: WWW/HTTP",
        "Topic :: Software Development :: Libraries :: Python Modules",
    ],
)
