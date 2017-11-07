from random import uniform
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

    complete_result = [min_max[MIN], min_max[MIN]] + result + [min_max[MAX], min_max[MAX]]
    return complete_result


# From a cut and a vertex "a" on the left side, compute the vertex on the right side, passing in the mid of the cut
def compute_b(a, cut):
    return (cut - a) * 2 + a


# From a list of left-most vertex and a cut series, return a
def compute_bounds(a_series, cut_series, min_max):
    result_a = [uniform(min_max[MIN], cut_series[0])]
    result_lb = [min_max[MIN]]
    result_ub = [cut_series[0]]

    for i in range(1, len(a_series)):
        ith_lb = compute_b(result_a[i - 1], cut_series[i - 1])
        ith_ub = cut_series[i]
        ith_a = uniform(ith_lb, ith_ub)

        result_lb.append(ith_lb)
        result_ub.append(ith_ub)
        result_a.append(ith_a)

    return [result_lb, result_ub]


"""
# From a vectorial representation of a trap series compute the standard deviation of the slopes
def get_slope_std(trap_series, depth):
    slope_list = get_slope_list(trap_series, depth)
    return np.std(slope_list)



def get_slope_sum(trap_series, depth):
    slope_list = get_slope_list(trap_series, depth)
    return np.sum(slope_list)
"""


def get_slope_list(trap_series, depth):
    def compute_segment_slope(x1, y1, x2, y2):
        if x1 == x2:
            x2 += 0.1
        if y1 == y2:
            y2 += 0.1

        return float(y2 - y1) / (x2 - x1)

    real_series = trap_series[2:-2]
    slope_list = []

    while len(real_series) > 0:
        c = real_series[0]
        d = real_series[1]
        x1 = c
        y1 = -depth
        x2 = d
        y2 = 0
        segment = compute_segment_slope(x1, y1, x2, y2)
        slope_list += [abs(segment)]
        real_series = real_series[2:]
    return slope_list
