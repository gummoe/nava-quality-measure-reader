import unittest

from main import get_file, SCHEMAS_FILE_PATH, SCHEMAS_FILE_TYPE


class MainTest(unittest.TestCase):

    def test_get_file_not_found(self):
        with self.assertRaises(FileNotFoundError):
            get_file('nope', SCHEMAS_FILE_PATH, SCHEMAS_FILE_TYPE)
