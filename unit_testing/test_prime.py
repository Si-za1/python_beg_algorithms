import unittest 
from prime import is_prime

class Testprimenumber(unittest.TestCase):
    def test_one(self):
        self.assertTrue(is_prime(2))
    def test_two(self):
        self.assertTrue(is_prime(5))



if __name__ == "__main__":
    unittest.main()