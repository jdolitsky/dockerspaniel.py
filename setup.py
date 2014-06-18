#!/usr/bin/env python

import os
from distutils.core import setup

r_txt = os.path.join(os.path.dirname(os.path.realpath(__file__)), 'requirements.txt')

with open(r_txt) as f:
    required = f.read().splitlines()

setup(name='dockerspaniel',
      version='0.1.2',
      description='Create Dockerfiles from JSON',
      author='Josh Dolitsky',
      author_email='jdolitsky@gmail.com',
      url='https://github.com/jdolitsky/dockerspaniel.py',
      download_url='https://github.com/jdolitsky/dockerspaniel.py/tarball/0.1.2',
      packages=['dockerspaniel'],
      keywords=['docker','dockerfile','json','dockerspaniel','spaniel','spanielfile'],
      install_requires=required,
      classifiers=[],
     )
