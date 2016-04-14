latexbuild
==========

This is a recent effort at writing a very light Latex build wrapper for
Python 3 using Jinja2 templates. It was inspired by the build philosophy
found in http://pythonhosted.org/latex/ . However, the original latex
library made it difficult to do complex, non-pdf builds (such as
compiling to HTML). This repository creates simple components that can
be used to build Latex from Jinja2 templates without losing control of
the lower-level command line tools provided with latex (like pdflatex
and htlatex). The usefulness of the library is split into two
components:

1. Rendering Jinaj2 templates for Latex
2. Compiling the rendered template with Latex

Rendering Jinja2 templates for Latex
------------------------------------

Latex is a great typesetting engine for large, complex projects.
However, its native build tools lack a straightforward templating engine
where multiple people can collaborate on a similar document. For
example, imagine a scenario where five professors in the same department
need to create a course syllabus. Grading requirements may be
standardized at the department level, which individual lessons are up to
the professors. If course syllabuses were created using Jinja2
templating and Latex, the department could create a base template that
listed the department standards and ask the professors to extend the
base template for each course's syllabus. That way, the professors need
not worry about cross-course content or department-wide formatting
requirements: these would be handled by the base template.

Assume the department saves the following content in *template.tex*:

.. code:: tex

    % FILENAME: template.tex
    \documentclass[12pt]{article}

    \title{Economics Departmnt: \BLOCK{block title}\BLOCK{endblock}}
    \author{\vspace{-5ex}}
    \date{\vspace{-5ex}}

    \begin{document}
    \maketitle

    \section{Department Introduction}
    This is a standard message from the department
    that will appear in every syllabus in exactly this place.
    Professors shouldn't have to think about this.

    \section{Greatness}
    \BLOCK{block greatness}\BLOCK{endblock}

    \section{Boredom}
    \BLOCK{block boredom}\BLOCK{endblock}

    \end{document}

Now that the temlate has been created, the accounting professor can
create his syllabus in the following way:

.. code:: tex

    %- extends "template.tex"

    % FILENAME: accounting.tex

    %- block title
    Accounting
    %- endblock

    %- block greatness
    This is a great, accounting-specific block
    %- endblock

    %- block boredom
    This is a boring, accounting-specific block
    %- endblock

Additionally, the statistics professor can create her syllabus as
follows:

.. code:: tex

    %- extends "template.tex"

    % FILENAME: statistics.tex

    %- block title
    Statistics for juggernauts
    %- endblock

    %- block greatness
    This is a great, statistics-specific block
    %- endblock

    %- block boredom
    This is a boring, statistics-specific block
    %- endblock

Most Jinja2 templating functionality is supported, using the same syntax
alterations as the latex python package referenced in this README's
introduction. For example, if you would like to loop over values and
place them in a Latex list, you may use the following code.

.. code:: tex

    This snipped provides an ordered list over the list variable passed from Python:

    \begin{enumerate}
      %- for variable in variable_list
      \item \VAR{variable}
      %- endfor
    \end{enumerate}

    Alternatively, snippet provides an unordered list over the list variable passed from Python:

    \begin{itemize}
      %- for variable in variable_list
      \item \VAR{variable}
      %- endfor
    \end{itemize}

This section will continue being updated over time with more examples.

Building Latex Output
---------------------

For the simplest project, you can build a Jinja2-templated latex source
repository with the following code:

.. code:: python

    from latexbuild import build_pdf, build_html, render_latex_template

    PATH_JINJA2 = "/path/to/your/latex/jinja2/root"
    PATH_TEMPLATE_RELATIVE_TO_PATH_JINJA2 = "template/filepath.tex"
    PATH_OUTPUT_PDF = "/path/to/your/output/directory/MYOUTPUTFILE.pdf"
    PATH_OUTPUT_HTML = "/path/to/your/output/directory/MYOUTPUTFILE.html"

    # Build Jinja2 template, compile result latex, move compiled file to output path,
    # and clean up all intermediate files
    build_pdf(PATH_JINJA2, PATH_TEMPLATE_RELATIVE_TO_PATH_JINJA2, PATH_OUTPUT_PDF)
    build_html(PATH_JINJA2, PATH_TEMPLATE_RELATIVE_TO_PATH_JINJA2, PATH_OUTPUT_HTML)

    # If you just want the rendered template's text in a python variable, do the following (assuming you have no variables to pass):
    render_latex_template(PATH_JINJA2, PATH_TEMPLATE_RELATIVE_TO_PATH_JINJA2)

    # If your template renders Jinja2 variables, most interfaces provide
    # a dictionary parameter. See below for an example for simply
    # rendering the template's text in Python
    DICT_VALS = {
        'var1': 'my variable 1 value',
        'list_var': ['item 1 for analysis', 'item 2 for analysis']
        }
    render_latex_template(
        PATH_JINJA2,
        PATH_TEMPLATE_RELATIVE_TO_PATH_JINJA2,
        DICT_VALS,
        )

For more complex builds, the system is designed to accept whatever
command line arguments you wish to use. Please see the source file
latexbuild/build.py and read the LatexBuild class's documentation for
more information.

Supported systems
-----------------

1. Tried only on Python 3.4
2. Tried only on Linux Mint 17.3

Written by
----------

Samuel Roeca
