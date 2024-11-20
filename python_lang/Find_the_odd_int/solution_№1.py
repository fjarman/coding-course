import unittest

def find_it(seq):
    a = []
    for i in range(len(seq)):
        if seq.count(seq[i]) != 0:
            a.append(seq.count(seq[i]) != 0)
    print(min(a))



class TestStringMethods(unittest.TestCase):

    def test_correct(self):
        self.assertEqual(find_it(4324435), 2)