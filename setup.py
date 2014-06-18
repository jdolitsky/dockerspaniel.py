#!/usr/bin/env python

from distutils.core import setup

with open('requirements.txt') as f:
    required = f.read().splitlines()

setup(name='dockerspaniel',
      version='0.1.3',
      description='Create Dockerfiles from JSON',
      author='Josh Dolitsky',
      author_email='jdolitsky@gmail.com',
      url='https://github.com/jdolitsky/dockerspaniel.py',
      download_url='https://github.com/jdolitsky/dockerspaniel.py/tarball/0.1.3',
      packages=['dockerspaniel'],
      keywords=['docker','dockerfile','json','dockerspaniel','spaniel','spanielfile'],
      install_requires=required,
      classifiers=[],
     )
