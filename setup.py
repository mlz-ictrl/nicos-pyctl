#!/usr/bin/env python
# -- encoding: utf-8 --
from setuptools import setup, Extension

setup(name='nicos-pyctl',
      version='1.3',
      description='NICOS pyctl c module',
      author='Georg Brandl',
      author_email='georg.brandl@frm2.tum.de',
      url='https://forge.frm2.tum.de/simple/nicos-pyctl/',
      packages=['nicospyctl'],
      ext_modules=[Extension('nicospyctl.pyctl', ['pyctl.c'])],
     )
