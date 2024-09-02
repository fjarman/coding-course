import unittest

def sort_dict(d):
    pairs = list(d.items())
    pairs.sort(key=lambda a: a[1], reverse=True)
    return pairs
class TestStringMethods(unittest.TestCase):

    def test_correct(self):
        #self.assertEqual(sort_dict({1:3,2:2,3:1}), [(1,3),(2,2),(3,1)])
        #self.assertEqual(sort_dict({3:1,2:2,1:3}), [(1,3),(2,2),(3,1)])
        #self.assertEqual(sort_dict({1:2,2:4,3:6}), [(3,6),(2,4),(1,2)])
        self.assertEqual(sort_dict({1: 5, 3: 10, 2: 2, 6: 3, 8: 8}), [(3, 10), (8, 8), (1, 5), (6, 3), (2, 2)])