import unittest

def duplicate_encode(word):
    word = word.lower()
    slovar = {}
    zamena = ""
    for i in range(len(word)):
        if word[i] not in slovar:
            slovar[word[i]] = 1
        else:
            slovar[word[i]] += 1
    for i in range(len(word)):
        if slovar[word[i]] > 1:
            zamena += ")"
        else:
            zamena += "("
    return zamena
class TestStringMethods(unittest.TestCase):

    def test_correct(self):
        #self.assertEqual(duplicate_encode("recede"),"()()()")
        #self.assertEqual(duplicate_encode("(( @"),"))((")
        self.assertEqual(duplicate_encode("Success"),")())())")