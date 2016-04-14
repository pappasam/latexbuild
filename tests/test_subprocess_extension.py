import os
import unittest
from subprocess import CalledProcessError
from latexbuild.subprocess_extension import check_output_cwd

#######################################################################
# Define constants
#######################################################################
PATH_FILE = os.path.abspath(__file__)
PATH_TEST = os.path.dirname(PATH_FILE)
PATH_MAIN = os.path.dirname(PATH_TEST)
NAME_FILE = os.path.basename(PATH_FILE)

#######################################################################
# Define helper functions
#######################################################################
def ls_and_split(directory):
    stdout, stderr = check_output_cwd(['ls'], directory)
    return stdout.decode().split('\n')

#######################################################################
# Main class
#######################################################################
class TestCheckOutputCwd(unittest.TestCase):

    def test_raises_bad_binary(self):
        self.assertRaises(ValueError,
                check_output_cwd, ['fjadklsjfkldsjf', '--ddfddf'], PATH_TEST)

    def test_raises_bad_call(self):
        self.assertRaises(CalledProcessError,
                check_output_cwd, ['python', '--ddfddf'], PATH_TEST)

    def test_ls_current_dir(self):
        self.assertIn(NAME_FILE, ls_and_split(PATH_TEST))

    def test_ls_above_dir(self):
        self.assertNotIn(NAME_FILE, ls_and_split(PATH_MAIN))

if __name__ == '__main__':
    unittest.main()
