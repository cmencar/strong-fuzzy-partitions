# coding=utf-8
import series_utilities as util
import numpy as np


def minimize_slope_std(a_series, *args):
    cuts_list, minmax_list, depth = args

    a_series_split = _split_series_for_dimension(a_series, cuts_list)
    trap_series_split = _rebuild_series(a_series_split, cuts_list, minmax_list)

    compute_slope_fun = util.arctan_segment_slope
    slope_multi_list = [util.get_slope_list(trap_series, depth, compute_slope_fun) for trap_series in trap_series_split]
    slope_std_list = [np.std(slope_list) for slope_list in slope_multi_list]

    result = sum(slope_std_list) / len(slope_std_list)
    return result


def minimize_slope_sum(a_series, *args):
    cuts_list, minmax_list, depth = args

    a_series_split = _split_series_for_dimension(a_series, cuts_list)
    trap_series_split = _rebuild_series(a_series_split, cuts_list, minmax_list)

    compute_slope_fun = util.arctan_segment_slope
    slope_multi_list = [util.get_slope_list(trap_series, depth, compute_slope_fun) for trap_series in trap_series_split]
    slope_sum_list = [sum(slope_list) for slope_list in slope_multi_list]

    result = sum(slope_sum_list) / len(slope_sum_list)
    return -result


def _split_series_for_dimension(a_series, cuts_list):
    result = []
    for i in range(0, len(cuts_list)):
        k = len(cuts_list[i])
        result.append(a_series[0:k])
        a_series = a_series[k:]
    return result


def _rebuild_series(a_series_split, cuts_list, minmax_list):
    result = []
    for i in range(0, len(a_series_split)):
        trap_series = util.generate_series(a_series_split[i], cuts_list[i], minmax_list[i])
        result.append(trap_series)
    return result
