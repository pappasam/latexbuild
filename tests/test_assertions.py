import unittest
import os
from latexbuild.assertions import (
        has_file_extension,
        is_binary,
        list_is_type,
        )

class TestHasFileExtensions(unittest.TestCase):
    '''Test class for has_file_extension'''

    def test_correct_extensions(self):
        test_vals = [
                ("hello.html", ".html"),
                ("/var/test.pdf", ".pdf"),
                ("fdasfdf/h.doc", ".doc"),
                ]
        for filename, ext in test_vals:
            self.assertTrue(has_file_extension(filename, ext))

    def test_wrong_extensions(self):
        test_vals = [
                ("hello.html", ".doc"),
                ("/var/test.pdf", ".html"),
                ("fdasfdf/.doc", ".docx"),
                ]
        for filename, ext in test_vals:
            self.assertRaises(ValueError, has_file_extension, filename, ext)

    def test_no_extension(self):
        self.assertTrue(has_file_extension("/var/hello", ""))

class TestIsBinary(unittest.TestCase):
    '''Test class for is_binary'''

    def test_raises_typeerror(self):
        bad_inputs = [
                1, ['hello', 'world'], 12.3, ("my", "goodness"),
                ]
        for bad_input in bad_inputs:
            self.assertRaises(TypeError, is_binary, bad_input)

    def test_raises_valueerror(self):
        invalid_binaries = [
                "fljdlaksjflkdjf", "not system binary", "python345",
                ]
        for invalid_binary in invalid_binaries:
            self.assertRaises(ValueError, is_binary, invalid_binary)

    def test_true_valid_binary(self):
        valid_binaries = ['python', 'ls', 'grep']
        for valid_binary in valid_binaries:
            self.assertTrue(is_binary(valid_binary))

class TestListIsType(unittest.TestCase):
    '''Test class for list_is_type'''

    def test_not_class(self):
        class_instances = [1, "stringval", 14.5]
        for class_instance in class_instances:
            self.assertRaises(TypeError, list_is_type, [], class_instance)

    def test_not_list(self):
        not_lists = [1, (1, 2, 3), "helloworld"]
        for not_list in not_lists:
            self.assertRaises(TypeError, list_is_type, not_list, str)

    def test_bad_lists(self):
        bad_lists = [
                ["hello", 1],
                [1, 2, 3, 4],
                ["hello", ("world", "man")],
                ]
        for bad_list in bad_lists:
            self.assertRaises(TypeError, list_is_type, bad_list, str)

    def test_good_lists(self):
        good_lists = [
                ["hello", "world"],
                ["hello"],
                ["a", "b", "cdef"],
                ]
        for good_list in good_lists:
            self.assertTrue(list_is_type(good_list, str))

if __name__ == '__main__':
    unittest.main()
