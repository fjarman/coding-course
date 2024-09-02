import unittest

def user_contacts(data):
    json = {}
    for i in range(len(data)):
        if len(data[i]) == 1:
            json[data[i][0]] = None
        else:
            json[data[i][0] = data[i][1]
    return json

class TestStringMethods(unittest.TestCase):

    def test_correct(self):
        self.assert_equals(user_contacts([["Grae Drake", 98110], ["Bethany Kok"], ["Alex Nussbacher", 94101], ["Darrell Silver", 11201]]), {'Grae Drake': 98110, 'Darrell Silver': 11201, 'Alex Nussbacher': 94101, 'Bethany Kok': None})
