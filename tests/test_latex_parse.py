import unittest
from latexbuild.latex_parse import (
        escape_latex_str_if_str,
        )

class TestLatexParse(unittest.TestCase):
    '''Test class for escape_latex_str'''

    def test_escape_chars(self):
        in_s = r"$%\$#_\{}~^"
        out_s = r"\$\%\$\#\_\{\}\~\^"
        self.assertEqual(escape_latex_str_if_str(in_s), out_s)

    def test_with_backslash(self):
        in_s = r"$%\$#_\\\{}~^"
        out_s = r"\$\%\$\#\_\\\{\}\~\^"
        self.assertEqual(escape_latex_str_if_str(in_s), out_s)

    def test_multiline_str(self):
        in_s = r'''this is \a very great string
        and I couldn't ever_want to make too \\ much money$'''
        out_s = r'''this is \\a very great string
        and I couldn't ever\_want to make too \\ much money\$'''
        self.assertEqual(escape_latex_str_if_str(in_s), out_s)

    def test_non_string_returns_original_value(self):
        for non_string_value in [
            123,
            11.5,
            ['hello', 'world'],
            {1:2, 3:4},
        ]:
            self.assertEqual(
                non_string_value,
                escape_latex_str_if_str(non_string_value),
            )

if __name__ == '__main__':
    unittest.main()
