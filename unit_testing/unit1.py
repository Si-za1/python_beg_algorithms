import unittest 

class TestStringMethods(unittest.TestCase):
    def test_lower(self):
        self.assertEqual('foo'.islower(), True)

    def test_upper(self):
        self.assertEqual('foo'.isupper(), 'FOO')
    
        


if __name__ == '__main__':
    unittest.main()
