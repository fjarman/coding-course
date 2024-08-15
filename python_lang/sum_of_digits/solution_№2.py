import unittest
def digital_root(n):
    counter = 0
    string = str(n)
    com = len(string)
    for i in range(com):
        counter += int(string[i])
        n = counter
    return digital_root(n)

class TestStringMethods(unittest.TestCase):

    def test_correct(self):
        self.assertEqual(digital_root(999999999999999999999999999999), 1)