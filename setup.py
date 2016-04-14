"""Setup latexbuild python package"""

import os
from setuptools import setup, find_packages

# Set directories
PATH_MAIN = os.path.dirname(os.path.abspath(__file__))
FILE_README = os.path.join(PATH_MAIN, 'README.rst')

# Readme
with open(FILE_README, 'r') as readme:
    long_description = readme.read()

setup(
        name='latexbuild',
        version='0.0.1',
        description='Building Jinja2 templates with latex',
        long_description=long_description,
        url='https://github.com/pappasam/latexbuild',
        author='Samuel Roeca',
        author_email='samuel.roeca@gmail.com',
        license='MIT',
        classifiers=[
            'Development Status :: 3 - Alpha',
            'Intended Audience :: Developers',
            'Topic :: Software Development :: Build Tools',
            'Topic :: Text Processing :: Markup :: LaTeX',
            'Topic :: Software Development :: Libraries :: Python Modules',
            'Topic :: Utilities',
            'License :: OSI Approved :: MIT License',
            'Natural Language :: English',
            'Operating System :: POSIX :: Linux',
            'Programming Language :: Python :: 3 :: Only',
            ],
        keywords='latex jinja2 build html texlive',
        packages=find_packages(exclude=[
            'tests*',
            'venv*',
            'build_readme.py',
            ]),
        install_requires=[
            'Jinja2>=2.8',
            ],
        )
