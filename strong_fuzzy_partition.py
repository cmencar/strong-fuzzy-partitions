"""
    Generate a vectorial representation of a strong fuzzy partition
    Algorithm and notation are taken from the paper: "Design of Strong Fuzzy Partition"
    Link: https://www.researchgate.net/publication/266644545_Design_of_Strong_Fuzzy_Partitions_from_Cuts
"""

import numpy as np

MIN = 0
MAX = 1
LEFT_BOUND = 0
A = 0
B = 1
C = 2
D = 3
ERR_VALUE = float('nan')


def constant_slope(cuts_list, minmax_list):
    assert len(cuts_list) == len(minmax_list)

    result = []
    dimension = len(cuts_list)
    for d in range(0, dimension):
        dimension_series = _constant_slope_single_dimension(cuts_list[d], minmax_list[d])
        result.append(dimension_series)
    return result


"""
def _constant_slope_single_dimension(cuts, min_max):
    slope = _compute_slope(cuts, min_max)
    dummy = min_max[MIN]
    dummy_trap = [dummy, dummy, min_max[MIN], min_max[MIN]]
    prev = dummy_trap
    trap_series = prev

    for i in range(0, len(cuts)):
        trap = _build_single_trap(cuts[i], slope, prev)
        trap_series += [trap[C], trap[D]]
        prev = trap
    trap_series += [min_max[MAX], min_max[MAX]]

    dummy_vertex = 2
    trap_series = trap_series[dummy_vertex:]
    return trap_series
"""


def _constant_slope_single_dimension(cuts, minmax):
    slope = _compute_slope(cuts, minmax)
    traps = [[ERR_VALUE, ERR_VALUE, ERR_VALUE, ERR_VALUE] for i in range(0, len(cuts) + 1)]
    for i in range(0, len(cuts)):
        traps[i + 1][A] = cuts[i] - (1 / (2 * slope))
        traps[i + 1][B] = cuts[i] + (1 / (2 * slope))
        traps[i][C] = traps[i + 1][0]
        traps[i][D] = traps[i + 1][1]
    traps[0][A] = minmax[0]
    traps[0][B] = minmax[0]
    traps[-1][C] = minmax[1]
    traps[-1][D] = minmax[1]
    return traps


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


def _build_single_trap(cut, slope, prev_trap):
    a = prev_trap[C]
    b = prev_trap[D]
    c = cut + (float(1) / 2 * -slope)
    d = cut - (float(1) / 2 * -slope)
    return [a, b, c, d]
