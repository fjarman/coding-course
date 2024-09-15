import unittest


def mnojiteli(chislo):
    spisok_1 = []
    for i in range(2, chislo // 2 + 1):
        if chislo % i == 0:
            spisok_1.append(i)
    return spisok_1

def find_combinations_for(n, head_index, product, factors, current_path, paths):
    counter = 0
    new_head_index = head_index
    while new_head_index >= 0:
        current_local_path = current_path[:]
        current_local_path.append(factors[new_head_index])
        if factors[new_head_index] * product == n:
            counter += 1
            paths.append(current_local_path)
        if factors[new_head_index] * product < n:
            counter += find_combinations_for(n, new_head_index, product * factors[new_head_index], factors, current_local_path, paths)
        new_head_index -= 1
    return counter

def find_combinations(n):
    factors = mnojiteli(n)
    paths = []
    combinations = find_combinations_for(n, len(factors) - 1, 1, factors, [], paths) + 1
    print(paths)
    return combinations

class TestStringMethods(unittest.TestCase):

    def test_correct(self):
        self.assertEqual(find_combinations(960), 105)