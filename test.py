"""import unittest

import sfp_generation
from data import TrapSFP, TrapSeries


def fun(x):
    return x + 1


class MyTest(unittest.TestCase):
    def test_compute_slope(self):
        cuts = [3, 8, 15, 23]
        min_max = [2, 25]

        computed = sfp_generation._compute_slope(cuts, min_max)
        expected = 0.5
        self.assertEqual(computed, expected)

    def test_data(self):
        actual = TrapSeries(TrapSFP([0, 0, 2, 2]))
        actual.append(TrapSFP([2, 2, 2.75, 3.25]))
        actual.append(TrapSFP([2.75, 3.25, 7.75, 8.25]))
        actual.append(TrapSFP([7.75, 8.25, 14.75, 15.25]))
        actual.append(TrapSFP([14.75, 15.25, 22.75, 23.25]))
        actual.append(TrapSFP([22.75, 23.25, 25, 25]))

        expected = [0, 0, 2, 2, 2.75, 3.25, 7.75, 8.25, 14.75, 15.25, 22.75, 23.25, 25, 25]
        self.assertEqual(str(actual), str(expected))

    def test_build_single_trapeze(self):
        cut = 5
        slope = 1
        prev_trapeze = TrapSFP([1, 2, 3, 4])

        computed = sfp_generation._build_single_trap(cut, slope, prev_trapeze)
        expected = TrapSFP([3, 4, 4.5, 5.5])
        self.assertEqual(computed, expected)


if __name__ == '__main__':
    unittest.main()
"""""""""