import unittest
from HW_4 import FahToCel, fibonacci

class TestHW(unittest.TestCase):
    def test_FahToCel(self):
        self.assertEqual(FahToCel(32), 0.0)
        self.assertEqual(FahToCel(212), 100.0)
        self.assertEqual(FahToCel(-40), -40.0)
        self.assertAlmostEqual(FahToCel(93), 33.88888888888889, places=4)
    
    def test_fibonacci(self):
        self.assertEqual(fibonacci(0), 0)
        self.assertEqual(fibonacci(1), 1)
        self.assertEqual(fibonacci(2), 1)
        self.assertEqual(fibonacci(3), 2)
        self.assertEqual(fibonacci(4), 3)
        self.assertEqual(fibonacci(5), 5)
        self.assertEqual(fibonacci(6), 8)
    
if __name__ == '__main__':
    unittest.main()