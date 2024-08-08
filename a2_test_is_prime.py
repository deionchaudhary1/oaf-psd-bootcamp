import unittest
from a2_is_prime import is_prime

'''
Function that tests the is_prime function in is_prime.py
'''

class TryTesting(unittest.TestCase):
    def test_functional(self):
        self.assertTrue(is_prime(11))
        self.assertFalse(is_prime(4))
        self.assertTrue(is_prime(53))
    def test_nonfunctional(self):
        self.assertFalse(is_prime(0))
        self.assertFalse(is_prime(None))
        self.assertFalse(is_prime(-1))
        with self.assertRaises(TypeError):
            is_prime("hello")
            is_prime(3.283)
        

if __name__ == "__main__":
    unittest.main()