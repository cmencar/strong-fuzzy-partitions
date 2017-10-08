import numpy as np
from data import TrapezoidalSFP

MIN = 0
MAX = 1


def _compute_slope(cuts, min_max):
    assert isinstance(min_max, list)
    assert isinstance(cuts, list)

    first = 2 * min_max[MIN] - cuts[0]
    last = 2 * min_max[MAX] - cuts[-1]
    extended_cuts = [first] + cuts + [last]

    delta_vector = [abs(extended_cuts[idx + 1] - extended_cuts[idx]) for idx in range(len(extended_cuts) - 1)]
    delta_min_idx = int(np.argmin(delta_vector))

    t_min = cuts[delta_min_idx]
    t_plus = cuts[delta_min_idx + 1]

    b_min = c_min = float(t_plus + t_min) / 2
    a_min = 2 * t_min - b_min
    d_min = 2 * t_plus - c_min

    slope = float(1) / (b_min - a_min)
    return slope


def _build_first_trapeze(first_cut, min, slope):
    a_1 = min
    b_1 = min
    c_1 = first_cut - float(1) / (2 * slope)
    d_1 = first_cut + float(1) / (2 * slope)
    return TrapezoidalSFP(a_1, b_1, c_1, d_1)


def _build_trapezes_from_first(cuts, slope, min_max):
    result = []
    prev = _build_first_trapeze(cuts[0], slope, min_max[MIN])
    result += [prev]
    for i in range(1, len(cuts) - 1):
        new_trapeze = _build_single_trapeze(cuts[i], slope, prev)
        result += [new_trapeze]
        prev = new_trapeze
    return result


def _build_single_trapeze(cut, slope, prev_trapeze):
    assert isinstance(prev_trapeze, TrapezoidalSFP)

    a = prev_trapeze.c
    b = prev_trapeze.d
    c = cut + (float(1) / 2 * -slope)
    d = cut - (float(1) / 2 * -slope)
    return TrapezoidalSFP(a, b, c, d)
