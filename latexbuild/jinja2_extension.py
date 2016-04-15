"""Latex-specific Jinja2 configurations and functions

This module provides a template-rendering function for Jinja2
that overrides Jinja2 defaults to make it work more seamlessly
with Latex.
"""

import jinja2
import re

######################################################################
# J2_ARGS
#   Constant was borrowed from Marc Brinkmann's
#   latex repository (mbr/latex on github)
######################################################################
J2_ARGS = {
        'block_start_string': r'\BLOCK{',
        'block_end_string': '}',
        'variable_start_string': r'\VAR{',
        'variable_end_string': '}',
        'comment_start_string': r'\#{',
        'comment_end_string': '}',
        'line_statement_prefix': '%-',
        'line_comment_prefix': '%#',
        'trim_blocks': True,
        'autoescape': False,
        }

######################################################################
# Latex escape regex constants
######################################################################
ESCAPE_CHARS = [r'\&', '%', r'\$', '#', '_', r'\{', r'\}', '~', r'\^', ]
ESCAPE_CHARS_OR = '[{}]'.format('|'.join(ESCAPE_CHARS))
REGEX_ESCAPE_CHARS = [
        (re.compile(r"(?=[^\\])" + i), r"\\" + i.replace('\\', ''))
        for i in ESCAPE_CHARS
        ]
REGEX_BACKSLASH = re.compile(r'\\(?!{})'.format(ESCAPE_CHARS_OR))

######################################################################
# Declare module functions
######################################################################
def escape_latex_str(string_text):
    '''Escape a latex string'''
    for regex, replace_text in REGEX_ESCAPE_CHARS:
        string_text = re.sub(regex, replace_text, string_text)
    string_text = re.sub(REGEX_BACKSLASH, r'\\\\', string_text)
    return string_text

def render_latex_template(path_templates, template_filename,
        template_vars=None):
    '''Render a latex template, filling in its template variables

    :param path_templates: the path to the template directory
    :param template_filename: the name, rooted at the path_template_directory,
        of the desired template for rendering
    :param template_vars: dictionary of key:val for jinja2 variables
        defaults to None for case when no values need to be passed
    '''
    var_dict = template_vars if template_vars else {}
    j2_env = jinja2.Environment(
            loader=jinja2.FileSystemLoader(path_templates), **J2_ARGS
            )
    template = j2_env.get_template(template_filename)
    var_dict_escape = {k:escape_latex_str(v) for k, v in var_dict.items()}
    return template.render(**var_dict_escape)
