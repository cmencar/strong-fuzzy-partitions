import unittest

import sfp_generation
from data import TrapezoidalSFP, TrapSeries


def fun(x):
    return x + 1


class MyTest(unittest.TestCase):
    def test_compute_slope(self):
        cuts = [3, 8, 15, 23]
        min_max = [2, 25]

        computed = sfp_generation._compute_slope(cuts, min_max)
        expected = 0.5
        self.assertEqual(computed, expected)

    def test_build_single_trapeze(self):
        cut = 5
        slope = 1
        prev_trapeze = TrapezoidalSFP(1, 2, 3, 4)

        computed = sfp_generation._build_single_trap(cut, slope, prev_trapeze)
        expected = TrapezoidalSFP(3, 4, 4.5, 5.5)
        self.assertEqual(computed, expected)

    def test_vectorize_trap_series(self):
        t1 = TrapezoidalSFP(1, 2, 3, 4)
        t2 = TrapezoidalSFP(3, 4, 5, 6)
        t3 = TrapezoidalSFP(5, 6, 7, 8)
        t4 = TrapezoidalSFP(7, 8, 9, 10)

        computed = TrapSeries([t1, t2, t3, t4]).vectorize()
        expected = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
        self.assertEqual(computed, expected)


if __name__ == '__main__':
    unittest.main()
