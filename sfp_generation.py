from data import TrapezoidalSFP, TrapSeries
import numpy as np

MIN = 0
MAX = 1
LEFT_BOUND = 0


def constant_slope(cuts, min_max):
    assert isinstance(cuts, list)
    assert isinstance(min_max, list)

    slope = _compute_slope(cuts, min_max)
    prev = _build_first_trap(LEFT_BOUND, min_max[MIN])
    trap_series = TrapSeries([prev])

    for i in range(0, len(cuts)):
        trap = _build_single_trap(cuts[i], slope, prev)
        trap_series.add_trap(trap)
        prev = trap

    last_trap = TrapezoidalSFP(prev.c, prev.d, min_max[MAX], min_max[MAX])
    trap_series.add_trap(last_trap)
    return trap_series


def _compute_slope(cuts, min_max):
    first_cut = 2 * min_max[MIN] - cuts[0]
    last_cut = 2 * min_max[MAX] - cuts[-1]
    extended_cuts = [first_cut] + cuts + [last_cut]

    delta_vector = [extended_cuts[idx + 1] - extended_cuts[idx] for idx in range(len(extended_cuts) - 1)]
    # delta_vector = [abs(diff) for diff in delta_vector] ...yes or no?
    delta_min_idx = int(np.argmin(delta_vector))

    t_min = extended_cuts[delta_min_idx]
    t_min_next = extended_cuts[delta_min_idx + 1]
    slope = float(1) / (t_min_next - t_min)
    return slope


def _build_first_trap(left_bound, min_value):
    return TrapezoidalSFP(left_bound, left_bound, min_value, min_value)


def _build_single_trap(cut, slope, prev_trapeze):
    assert isinstance(prev_trapeze, TrapezoidalSFP)

    a = prev_trapeze.c
    b = prev_trapeze.d
    c = cut + (float(1) / 2 * -slope)
    d = cut - (float(1) / 2 * -slope)
    return TrapezoidalSFP(a, b, c, d)
