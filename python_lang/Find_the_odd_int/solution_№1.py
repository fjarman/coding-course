import unittest

def find_it(seq):
    for i in range(len(seq)):
       if seq.count(seq[i]) % 2 != 0:
            return seq[i]



class TestStringMethods(unittest.TestCase):

    def test_correct(self):
        self.assertEqual(find_it(4324435), 2)