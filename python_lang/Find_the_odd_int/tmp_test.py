import unittest

def vernut_2_znacheniya():
    return 1, 2

class TestStringMethods(unittest.TestCase):

    def test_correct(self):
        self.assertEqual(vernut_2_znacheniya(), (1, 2))