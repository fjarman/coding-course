import unittest

def digital_root(n):
    while n > 10 or n == 10:
        counter = 0
        string = str(n)
        com = len(string)
        for i in range(com):
            counter += int(string[i])
        n = counter
        print(n)
    return n

class TestStringMethods(unittest.TestCase):

    def test_correct(self):
        self.assertEqual(digital_root(435439), 1)