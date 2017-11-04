import series_utilities as util


def minimize_slope_std(a_series, *args):
    cuts_list, minmax_list, depth = args

    a_series_split = _split_series_for_dimension(a_series, cuts_list)
    trap_series_split = _rebuild_series(a_series_split, cuts_list, minmax_list)
    slope_std_list = [util.get_slope_std(trap_series, depth) for trap_series in trap_series_split]
    result = sum(slope_std_list) / len(slope_std_list)
    return result


def minimize_slope_sum(a_series, *args):
    cuts_list, minmax_list, depth = args

    a_series_split = _split_series_for_dimension(a_series, cuts_list)
    trap_series_split = _rebuild_series(a_series_split, cuts_list, minmax_list)
    slope_sum_list = [util.get_slope_sum(trap_series, depth) for trap_series in trap_series_split]
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


def con(series, *args):
    tmp = [series[0]]
    for i in range(1, len(series)):
        tmp.append(series[i] - series[i - 1])
    zeros = [series for series in tmp if series == 0]
    if len(zeros) > 1:
        return [0]
    else:
        return [1]
