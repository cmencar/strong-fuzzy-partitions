import unittest

import strong_fuzzy_partition
from data import TrapezoidalSFP


def fun(x):
    return x + 1


class MyTest(unittest.TestCase):
    def test_compute_slope(self):
        cuts = [3, 8, 15, 23]
        min_max = [2, 25]

        computed = strong_fuzzy_partition._compute_slope(cuts, min_max)
        expected = 0.5
        self.assertEqual(computed, expected)

    def test_build_first_trapeze(self):
        first_cut = 3
        slope = 1
        min_value = 2

        computed = strong_fuzzy_partition._build_first_trapeze(first_cut, min_value, slope)
        expected = TrapezoidalSFP(2, 2, 2.5, 3.5)
        self.assertEqual(computed, expected)

    def test_build_single_trapeze(self):
        cut = 5
        slope = 1
        prev_trapeze = TrapezoidalSFP(1, 2, 3, 4)

        computed = strong_fuzzy_partition._build_single_trapeze(cut, slope, prev_trapeze)
        expected = TrapezoidalSFP(3, 4, 4.5, 5.5)
        self.assertEqual(computed, expected)


if __name__ == '__main__':
    unittest.main()
