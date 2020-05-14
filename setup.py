#!/usr/bin/env python
# -- encoding: utf-8 --
from setuptools import setup, Extension

setup(name='nicos-pyctl',
      version = '1.1',
      description='NICOS pyctl c module',
      author='Georg Brandl',
      author_email='georg.brandl@frm2.tum.de',
      url='http://tacodb.frm2.tum.de/pub/python/',
      packages=['nicospyctl'],
      ext_modules=[Extension('nicospyctl.pyctl', ['pyctl.c'])],
     )
