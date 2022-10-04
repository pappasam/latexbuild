"""Latex-specific Jinja2 configurations and functions

This module provides a template-rendering function for Jinja2
that overrides Jinja2 defaults to make it work more seamlessly
with Latex.
"""

import jinja2
from .utils import recursive_apply
from .latex_parse import escape_latex_str_if_str

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
# Declare module functions
######################################################################
def render_latex_template(path_templates, template_filename,
        template_vars=None, filters=None):
    '''Render a latex template, filling in its template variables

    :param path_templates: the path to the template directory
    :param template_filename: the name, rooted at the path_template_directory,
        of the desired template for rendering
    :param template_vars: dictionary of key:val for jinja2 variables
        defaults to None for case when no values need to be passed
    :param filters: dictionary of key:val for jinja2 filters
        defaults to None for case when no values need to be passed
    '''
    var_dict = template_vars if template_vars else {}
    var_dict_escape = recursive_apply(var_dict, escape_latex_str_if_str)
    j2_env = jinja2.Environment(
            loader=jinja2.FileSystemLoader(path_templates), **J2_ARGS
            )
    if filters:
        j2_env.filters.update(filters)
    template = j2_env.get_template(template_filename)
    return template.render(**var_dict_escape)
