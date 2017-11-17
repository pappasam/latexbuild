#!/usr/bin/env python

import os
from latexbuild import build_pdf, render_latex_template

PATH_THIS = os.path.dirname(os.path.abspath(__file__))
PATH_JINJA2 = os.path.join(PATH_THIS, 'templates')
PATH_PDF = os.path.join(PATH_THIS, 'pdf')

# Generate the pdf files
build_pdf(
    path_jinja2=PATH_JINJA2,
    template_name='child1.tex',
    path_outfile=os.path.join(PATH_PDF, 'child1.pdf'),
)

build_pdf(
    path_jinja2=PATH_JINJA2,
    template_name='child2.tex',
    path_outfile=os.path.join(PATH_PDF, 'child2.pdf'),
)
