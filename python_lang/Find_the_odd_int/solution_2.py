import unittest


def find_it(seq):
    counters = {}
    for i in range(len(seq)):
        number = seq[i]
        if number not in counters:
            counters[number] = 1 # 20 -> 1;
        else:
            counters[number] = counters[number] + 1
    for key in counters.keys():
        if counters[key] % 2 != 0:
            return key

# 10100
#   XOR
# 00100
# 10000

class TestStringMethods(unittest.TestCase):

    def test_correct(self):
        self.assertEqual(find_it([20,1,1,2,2,3,3,5,5,4,20,4,5]), 5)