import unittest
from latexbuild.latex_parse import (
        escape_latex_str,
        )

class TestLatexParse(unittest.TestCase):
    '''Test class for escape_latex_str'''

    def test_escape_chars(self):
        in_s = r"$%\$#_\{}~^"
        out_s = r"\$\%\$\#\_\{\}\~\^"
        self.assertEqual(escape_latex_str(in_s), out_s)

    def test_with_backslash(self):
        in_s = r"$%\$#_\\\{}~^"
        out_s = r"\$\%\$\#\_\\\{\}\~\^"
        self.assertEqual(escape_latex_str(in_s), out_s)

    def test_multiline_str(self):
        in_s = r'''this is \a very great string
        and I couldn't ever_want to make too \\ much money$'''
        out_s = r'''this is \\a very great string
        and I couldn't ever\_want to make too \\ much money\$'''
        self.assertEqual(escape_latex_str(in_s), out_s)

if __name__ == '__main__':
    unittest.main()
