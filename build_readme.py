#!/usr/bin/env python

import os
import pandoc
from latexbuild.utils import read_file

PATH_MAIN = os.path.dirname(os.path.abspath(__file__))
FILE_README_MD = os.path.join(PATH_MAIN, 'README.md')
FILE_README_RST = os.path.join(PATH_MAIN, 'README.rst')

doc = pandoc.Document()
doc.markdown = read_file(FILE_README_MD).encode('utf-8')
long_description = doc.rst.decode('utf-8')

with open(FILE_README_RST, 'w') as readme_rst:
    readme_rst.write(long_description)
