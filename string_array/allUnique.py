'''
Is Unique: Implement an algorithm to determine if a string has all unique characters. What if you
cannot use additional data structures?
'''

import unittest


def is_unique(s):
    if len(s) > 128:
        return False

    char_set = [False for _ in range(128)]  # Create array of 128 length and set it to false
    # loop through the string and find out if we are revisiting any of the char from char_set
    for char in s:
        val = ord(char)
        if char_set[val]:
            return False
        char_set[val] = True
    return True


class Test(unittest.TestCase):
    dataT = [('abcd'), ('s4fad'), ('')]
    dataF = [('23ds2'), ('hb 627jh=j ()')]

    def test_unique(self):
        for test_string in self.dataT:
            actual = is_unique(test_string)
            self.assertTrue(actual)
        for test_string in self.dataF:
            actual = is_unique(test_string)
            self.assertFalse(actual)


if __name__ == '__main__':
    unittest.main()
