import unittest
from is_prime import is_prime

'''
Function that tests the is_prime function in is_prime.py
'''

class TryTesting(unittest.TestCase):
    def test_functional_1(self):
        self.assertTrue(is_prime(11))
    def test_functional_2(self):
        self.assertFalse(is_prime(4))
    def test_functional_3(self):
        self.assertTrue(is_prime(53))
    def test_nonfunctional_1(self):
        self.assertFalse(is_prime(0))
    def test_nonfunctional_2(self):
        self.assertFalse(is_prime(None))
    def test_nonfuncional_3(self):
        self.assertFalse(is_prime(-1))

if __name__ == "__main__":
    unittest.main()