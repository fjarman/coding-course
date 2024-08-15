from solution import digital_root

import unittest

class TestStringMethods(unittest.TestCase):

    def test_correct(self):
        self.assertEqual(digital_root(435439), 7)
