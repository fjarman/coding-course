import unittest
def get_count(sentence):
    counter = 0
    string = len(sentence)
    for i in range(string):
        if i == "a" or i == "e" or i == "i" or i == "i" or i == "o" or i == "u":
            counter += 1
    return counter

class TestStringMethods(unittest.TestCase):

    def test_correct(self):
        self.assertEqual(get_count("hello"), 2)