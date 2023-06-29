import unittest
import random
import sys
sys.path.append("Bubblesort Algorithm")
from bubblesort import sort

class Test(unittest.TestCase):
    def test_bubblesort_fixed(self):
        self.assertEqual(sort([4,3,2,1]), [1,2,3,4])
        self.assertEqual(sort([4,3,6,6,2,1]), [1,2,3,4,6,6])
        self.assertEqual(sort([8,8,8,8,8,8,7,9]), [7,8,8,8,8,8,8,9])

    def test_bubblesort_random(self):
        # 500 random test cases (takes around 10 seconds)
        for _ in range(500):
            # Test a list with length 200
            testcase = []
            for i in range(200):
                testcase.append(random.randint(0,1000000))

            # Test it using builtin sorted()
            self.assertEqual(sort(testcase), sorted(testcase))

if __name__ == "__main__":
    unittest.main()