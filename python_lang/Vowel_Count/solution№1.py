import unittest
def get_count(sentence):
    counter = 0
    string = len(sentence)
    for i in range(string):
        if sentence[i] == "a" or sentence[i] == "e" or sentence[i] == "i" or sentence[i] == "i" or sentence[i] == "o" or sentence[i] == "u":
            counter += 1
    return counter

class TestStringMethods(unittest.TestCase):

    def test_correct(self):
        self.assertEqual(get_count("hello"), 2)