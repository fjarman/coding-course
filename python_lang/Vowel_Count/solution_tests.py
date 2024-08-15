import unittest

class TestStringMethods(unittest.TestCase):

    def test_correct(self):
        self.assertEqual(get_count(hello), 2)
