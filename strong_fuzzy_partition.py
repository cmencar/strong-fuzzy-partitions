from data import TrapezoidalSFP
import numpy as np

MIN = 0
MAX = 1


def constant_slope(cuts, min_max):
    assert isinstance(cuts, list)
    assert isinstance(min_max, list)

    slope = _compute_slope(cuts, min_max)
    prev = _build_first_trapeze(cuts[0], min_max[MIN], slope)
    result = [prev]
    for i in range(1, len(cuts) - 1):
        new_trapeze = _build_single_trapeze(cuts[i], slope, prev)
        result += [new_trapeze]
        prev = new_trapeze
    result += [TrapezoidalSFP(prev.c, prev.d, min_max[MAX], min_max[MAX])]
    return result


def _compute_slope(cuts, min_max):
    first = 2 * min_max[MIN] - cuts[0]
    last = 2 * min_max[MAX] - cuts[-1]
    extended_cuts = [first] + cuts + [last]

    delta_vector = [extended_cuts[idx + 1] - extended_cuts[idx] for idx in range(len(extended_cuts) - 1)]
    # delta_vector = [abs(diff) for diff in delta_vector] ...yes or no?
    delta_min_idx = int(np.argmin(delta_vector))

    t_min = extended_cuts[delta_min_idx]
    t_min_next = extended_cuts[delta_min_idx + 1]

    slope = float(1) / (t_min_next - t_min)
    return slope


def _build_first_trapeze(first_cut, min_value, slope):
    c_1 = first_cut + float(1) / (2 * -slope)
    d_1 = first_cut - float(1) / (2 * -slope)
    return TrapezoidalSFP(min_value, min_value, c_1, d_1)


def _build_single_trapeze(cut, slope, prev_trapeze):
    assert isinstance(prev_trapeze, TrapezoidalSFP)

    a = prev_trapeze.c
    b = prev_trapeze.d
    c = cut + (float(1) / 2 * -slope)
    d = cut - (float(1) / 2 * -slope)
    return TrapezoidalSFP(a, b, c, d)


"""
# Functional-way (just for fun)
def _build_trapezes_series(cuts, min_max, slope):
    def loop(cuts, slope, prev, result):
        if len(cuts) == 1:
            return result + [TrapezoidalSFP(prev.c, prev.d, min_max[MAX], min_max[MAX])]
        else:
            new_trapeze = _build_single_trapeze(cuts[0], slope, prev)
            return loop(cuts[1:], slope, new_trapeze, result + [new_trapeze])

    first_trapeze = _build_first_trapeze(cuts[0], min_max[MIN], slope)
    others = loop(cuts[1:], slope, first_trapeze, [])
    return [first_trapeze] + others
"""
