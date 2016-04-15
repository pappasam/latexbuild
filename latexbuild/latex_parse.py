"""Latex parsing functionality

This module provides functions to parse latex text
"""

import re

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
