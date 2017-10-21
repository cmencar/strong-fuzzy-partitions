import numpy as np
from random import uniform
import sfp_plot
import trap_utility

MIN = 0
MAX = 1
LEFT_BOUND = 0
A = 0
B = 1
C = 2
D = 3


def constant_slope(cuts, min_max):
    slope = _compute_slope(cuts, min_max)
    prev = _build_first_trap(LEFT_BOUND, min_max[MIN])
    trap_series = prev

    for i in range(0, len(cuts)):
        trap = _build_single_trap(cuts[i], slope, prev)
        trap_series += [trap[C], trap[D]]
        prev = trap

    trap_series += [min_max[MAX], min_max[MAX]]
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
    return [left_bound, left_bound, min_value, min_value]


def _build_single_trap(cut, slope, prev_trap):
    a = prev_trap[A]
    b = prev_trap[B]
    c = cut + (float(1) / 2 * -slope)
    d = cut - (float(1) / 2 * -slope)
    return [a, b, c, d]


def randomize_slope(trap_series):
    vec = trap_series[3:-1]
    for i in range(1, len(vec) - 1):
        vec[i] = uniform(vec[i - 1], vec[i + 1])
    return trap_series[0:3] + vec + [trap_series[-1]]


def get_slope_std(trap_series):
    slope_list = []
    real_series = trap_series[4:-2]

    while real_series:
        slope_list += [abs(real_series[0] - real_series[1])]
        real_series = real_series[2:]

    return np.std(slope_list)


def plot(cuts, min_max, trap_series, depth):
    split_series = trap_utility.split_in_trap(trap_series)
    sfp_plot.plot_trapeze_series(cuts, min_max, split_series, depth)
