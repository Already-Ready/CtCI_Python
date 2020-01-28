import unittest

def urlify(string):

    sum_string = ""
    string = string.rstrip().lstrip()
    for s in string:
        if s == " ":
            sum_string += "%20"
        else:
            sum_string += s

    return sum_string


class Test(unittest.TestCase):

    test = [('much ado about nothing      ', 'much%20ado%20about%20nothing'),
            ('Mr John Smith    ', 'Mr%20John%20Smith')]

    def test_urlify(self):
        for [test_string, expected] in self.test:
            result = urlify(test_string)
            self.assertEqual(result,expected)


if __name__ == "__main__":
    unittest.main()
