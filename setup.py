#!/usr/bin/env python
# -*- encoding: utf-8 -*-
from setuptools import setup

name='printerpkg'
description='Utility for creating pkgs to install os x printers.'
version='1'

author='Benedicte Emilie Brækken'
author_email='b.e.brakken@usit.uio.no'

packages=['printerpkg', 'printerpkg.resources']
install_requires=[]

scripts=['bin/gen-printer-pkg']

setup(name=name,
      version=version,
      description=description,
      author=author,
      author_email=author_email,
      packages=packages,
      install_requires=install_requires,
      include_package_data=True,
      scripts=scripts)
