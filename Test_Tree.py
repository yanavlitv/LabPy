import unittest
from Tree import gen_bin_tree

class TestTwoSum(unittest.TestCase):
    def test_tree_0(self):
        self.assertEqual(gen_bin_tree(0, 10), [])
    def test_tree_1(self):
        self.assertEqual(gen_bin_tree(1, 10), [10])
    def test_tree_2(self):
        self.assertEqual(gen_bin_tree(2, 10), [10, 31, 29])
    def test_tree_3(self):
        self.assertEqual(gen_bin_tree(3, 10), [10, 31, 29, 94, 92, 88, 86])
    def test_tree_4(self):
        self.assertEqual(gen_bin_tree(4, 10), [10, 31, 29, 94, 92, 88, 86, 283, 281, 277, 275, 265, 263, 259, 257])
    def test_tree_5(self):
        self.assertEqual(gen_bin_tree(5, 10), [10, 31, 29, 94, 92, 88, 86, 283, 281, 277, 275, 265, 263, 259, 257, 850, 848, 844, 842, 832, 830, 826, 824, 796, 794, 790, 788, 778, 776, 772, 770])


if __name__ == '__main__':
    unittest.main()
