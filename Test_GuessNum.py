import unittest
from GuessNum import guess_num

class Test_GuessNum(unittest.TestCase):

    def test_slow_search1(self):
        self.assertEqual(guess_num(4, 2, 6, 1), [4, 3])
    def test_slow_search2(self):
        self.assertEqual(guess_num(4, 6, 2, 1), [4, 3])
    def test_slow_search3(self):
        self.assertEqual(guess_num(6, 6, 16, 1), [6, 1])
    def test_slow_search4(self):
        self.assertEqual(guess_num(16, 6, 16, 1), [16, 11])
    def test_slow_search5(self):
        self.assertEqual(guess_num(6, 6, 6, 1), [6, 1])
    def test_slow_search6(self):
        self.assertEqual(guess_num(3, 7, 19, 1), [3, None])
    def test_slow_search7(self):
        self.assertEqual(guess_num(30, 7, 19, 1), [30, None])
    def test_bin_search1(self):
        self.assertEqual(guess_num(4, 2, 6, 2), [4, 2])
    def test_bin_search2(self):
        self.assertEqual(guess_num(4, 6, 2, 2), [4, 2])
    def test_bin_search3(self):
        self.assertEqual(guess_num(6, 6, 16, 2), [6, 3])
    def test_bin_search4(self):
        self.assertEqual(guess_num(16, 6, 16, 2), [16, 4])
    def test_bin_search5(self):
        self.assertEqual(guess_num(6, 6, 6, 2), [6, 1])
    def test_bin_search6(self):
        self.assertEqual(guess_num(3, 7, 19, 2), [3, None])
    def test_bin_search7(self):
        self.assertEqual(guess_num(30, 7, 19, 2), [30, None])



if __name__ == '__main__':
    unittest.main()
