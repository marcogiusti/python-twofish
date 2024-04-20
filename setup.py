"""
This file is part of Python Twofish
a Python bridge to the C Twofish library by Niels Ferguson

Released under The BSD 3-Clause License
Copyright (c) 2013 Keybase

setup.py - build and package info
"""

from setuptools import setup


setup(
    name="twofish",
    version="0.4.0",
    description="Bindings for the Twofish implementation by Niels Ferguson",
    author="Filippo Valsorda",
    author_email="filippo.valsorda@gmail.com",
    url="http://github.com/keybase/python-twofish",
    py_modules=["twofish"],
    setup_requires=["cffi>=1.0.0"],
    cffi_modules=["twofish_build.py:ffibuilder"],
    install_requires=["cffi>=1.0.0"],
    extras_require={
        "dev": [
            "black",
            "build",
            "mypy",
            "pycodestyle",
            "pyflakes",
            "tox",
            "types-cffi",
        ]
    },
    classifiers=[
        "Development Status :: 4 - Beta",
        "Intended Audience :: Developers",
        "License :: OSI Approved :: BSD License",
        "Programming Language :: Python :: 3.12",
        "Topic :: Security :: Cryptography",
        "Topic :: Software Development :: Libraries",
    ],
    license="3-clause BSD",
    long_description=open("README.rst").read(),
)
