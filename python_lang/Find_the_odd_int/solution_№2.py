import unittest

def find_it(seq):
    counter = 1
    for i in range(len(seq)):
       for j in range(len(seq)):
           if seq[i] == seq[j] and i != j:
               counter += 1
       if counter % 2 == 0:
           counter = 1
       else:
           return seq[i]



class TestStringMethods(unittest.TestCase):

    def test_correct(self):
        self.assertEqual(find_it([20,1,1,2,2,3,3,5,5,4,20,4,5]), 5)