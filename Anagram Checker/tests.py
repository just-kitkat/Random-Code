import unittest
import sys
sys.path.append("Anagram Checker")
from anagram import check

class Test(unittest.TestCase):
    def test_anagrams(self):
        self.assertTrue(check("Listen", "Silent"))
        self.assertTrue(check("Fried", "Fired"))
        self.assertTrue(check("sadder", "dreads"))

    def test_non_anagrams(self):
        self.assertFalse(check("Listens", "Silent"))
        self.assertFalse(check("Hello World", "Bye World"))
        self.assertFalse(check("hello", "yellow"))
        self.assertFalse(check("python", "javascript"))
        

if __name__ == "__main__":
    unittest.main()