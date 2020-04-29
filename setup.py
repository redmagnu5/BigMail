from setuptools import setup
import os
with open('requirements.txt') as f:
    installs = f.read().splitlines()

setup(name='BigMail',
      version='0.0.1',
      description='Mass emailer',
      author='Ethan P',
      url='redmagnu5@github.com',
      packages=['BigMail'],
      install_requires=installs,
      )
