import unittest

def duplicate_encode(word):
    x = '(' * len(word)
    for i in range(len(word)):
          if ((word.count(word[i]) == 2) or (word.count(word[i]) > 2)):
             zamena = word.replace(word, x)
             zamena_2 = word.replace(word[i], ')')
             return zamena_2
          else:
             zamena = word.replace(word, x)
             return zamena

class TestStringMethods(unittest.TestCase):

    def basic_test_cases():
        test.assert_equals(duplicate_encode("din"),"(((")
        test.assert_equals(duplicate_encode("recede"),"()()()")
        test.assert_equals(duplicate_encode("Success"),")())())","should ignore case")
        test.assert_equals(duplicate_encode("(( @"),"))((")