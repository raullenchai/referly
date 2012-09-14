import os
from setuptools import setup

setup(
    name='referly',
    version='1.0',
    author='Dr. (Raullen) Qi Chai',
    packages=['referly'],
    package_dir = {'referly' : 'lib'},
    description='Referly -- A python wrapper of referly REST API.',
)