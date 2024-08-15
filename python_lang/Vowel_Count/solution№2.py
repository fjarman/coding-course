import unittest

def get_count(sentence):
    counter = 0
    for character in sentence:
        if character == "a" or character == "e" or character == "i" or character == "i" or character == "o" or character == "u":
            counter += 1
    return counter

class TestStringMethods(unittest.TestCase):

    def test_correct(self):
        self.assertEqual(get_count("hello"), 2)