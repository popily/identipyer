from setuptools import setup
import os

try:
   import pypandoc
   long_description = pypandoc.convert('README.md', 'rst')
except (IOError, ImportError):
   long_description = open('README.md').read()

setup(name='identipyer',
      version='0.0.1',
      description='Identify semantic data types in tabular data',
      long_description=long_description,
      url='https://github.com/popily/identipyer',
      download_url ='https://github.com/popily/identipyer/tarball/0.0.1',
      author='Jonathon Morgan',
      author_email='jonathon@popily.com',
      license='MIT',
      packages=['identipyer'],
      test_suite='tests',
      install_requires=['python-dateutil','address','phonenumbers'],
      package_data = {
            'identipyer': ['data/*.csv'],
      },
      zip_safe=False)