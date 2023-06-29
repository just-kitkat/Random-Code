import unittest
import sys
sys.path.append("Binomial Expansion")
from binomial import expand

class Test(unittest.TestCase):
    def test_binomial_expansion(self):
        self.assertEqual(expand("(x+1)^0"), "1")
        self.assertEqual(expand("(x+1)^1"), "x+1")
        self.assertEqual(expand("(x+1)^2"), "x^2+2x+1")
        
        self.assertEqual(expand("(x-1)^0"), "1")
        self.assertEqual(expand("(x-1)^1"), "x-1")
        self.assertEqual(expand("(x-1)^2"), "x^2-2x+1")
        
        self.assertEqual(expand("(5m+3)^4"), "625m^4+1500m^3+1350m^2+540m+81")
        self.assertEqual(expand("(2x-3)^3"), "8x^3-36x^2+54x-27")
        self.assertEqual(expand("(7x-7)^0"), "1")
        
        self.assertEqual(expand("(-5m+3)^4"), "625m^4-1500m^3+1350m^2-540m+81")
        self.assertEqual(expand("(-2k-3)^3"), "-8k^3-36k^2-54k-27")
        self.assertEqual(expand("(-7x-7)^0"), "1")

if __name__ == "__main__":
    unittest.main()