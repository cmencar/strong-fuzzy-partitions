# coding=utf-8
from sympy import Symbol, limit
import numpy as np

MIN = 0
MAX = 1


# From a trap series [a1, b1, c1, d1, c2, d2, c3, d3] return a list of trap
# [[a1, b1, c1, d1], [a2, b2, c2, d2], [a3, b3, c3, d3]]
def split_in_trap(trap_series):
    def loop(series, acc):
        if len(series) < 4:
            return acc
        else:
            acc.append(series[0:4])
            return loop(series[2:], acc)

    return loop(trap_series, [])


# From vectorial representation of a trap series extract left-most vertex for every trap
def extract_a_series(trap_series):
    result = []

    # remove min and max value
    real_series = trap_series[2:-2]
    for i in range(0, len(real_series), 2):
        result += [real_series[i]]
    return result


# From a list of left-most vertex and a cut series, recreate the trap series in a vectorial representation
def generate_series(a_series, cut_series, min_max):
    result = []
    for i in range(0, len(a_series)):
        a = a_series[i]
        cut = cut_series[i]
        b = compute_b(a, cut)
        result += [a, b]

    result = [min_max[MIN], min_max[MIN]] + result + [min_max[MAX], min_max[MAX]]
    return result


# From a cut and a vertex "a" on the left side, compute the vertex on the right side, passing in the mid of the cut
def compute_b(a, cut):
    return (cut - a) * 2 + a


def compute_bounds(a_series, cuts, min_max):
    dummy_cuts = cuts + [min_max[MAX]]
    first_lb = min_max[MIN]
    first_lb = _fix_lb(first_lb, cuts[0], cuts[1])
    lb = [first_lb]
    ub = [dummy_cuts[0]]

    for i in range(1, len(a_series)):
        ith_lb = compute_b(lb[i - 1], dummy_cuts[i - 1])
        ith_lb = _fix_lb(ith_lb, dummy_cuts[i], dummy_cuts[i + 1])
        ith_ub = dummy_cuts[i]

        lb.append(ith_lb)
        ub.append(ith_ub)

    return [lb, ub]


def _fix_lb(lb_i, cut_i, cut_i_next):
    if compute_b(lb_i, cut_i) < cut_i_next:
        return lb_i

    while True:
        lb_i += 0.01
        if compute_b(lb_i, cut_i) < cut_i_next:
            return lb_i


def get_slope_list(trap_series, depth, compute_slope_func):
    real_series = trap_series[2:-2]
    slope_list = []

    while len(real_series) > 0:
        c = real_series[0]
        d = real_series[1]
        x1 = c
        y1 = -depth
        x2 = d
        y2 = 0
        segment = compute_slope_func(x1, y1, x2, y2)
        slope_list += [abs(segment)]
        real_series = real_series[2:]

    return slope_list


def arctan_segment_slope(x1, y1, x2, y2):
    dy = y2 - y1
    dx = x2 - x1

    x = Symbol('x')
    slope = limit(dy / x, x, dx)
    return np.arctan(float(slope))
