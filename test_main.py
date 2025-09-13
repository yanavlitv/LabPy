import unittest
from main import twosum

class TestTwoSum(unittest.TestCase):
    def test_two_sum_1(self):
        self.assertEqual(twosum([2,7,11,15], 9), [0, 1])
    def test_two_sum_2(self):
        self.assertEqual(twosum([2, 3, 4], 6), [0, 2])
    def test_two_sum_3(self):
        self.assertEqual(twosum([3, 3], 6), [0, 1])
    def test_two_sum_4(self):
        self.assertEqual(twosum([1, 2, 3, 4, 5], 10), None)
    def test_two_sum_5(self):
        self.assertEqual(twosum([1, 2, 5, 3.45], 6), None)
    def test_two_sum_6(self):
        self.assertEqual(twosum([2, 3, 4, '9'], 6), None)

if __name__ == '__main__':
    unittest.main()
