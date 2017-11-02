import series_utilities as util


def minimize_slope_std(a_series, *args):
    cuts_list, minmax_list, depth = args

    dimension_split = []
    for i in range(0, len(cuts_list)):
        k = len(cuts_list[i])
        dimension_split.append(a_series[0:k])
        a_series = a_series[k:]

    multi_trap_series = []
    for i in range(0, len(dimension_split)):
        trap_series = util.generate_series(dimension_split[i], cuts_list[i], minmax_list[i])
        multi_trap_series.append(trap_series)

    std_for_each_dimension = [util.get_slope_std(trap_series, depth) for trap_series in multi_trap_series]
    result = sum(std_for_each_dimension) / len(std_for_each_dimension)
    # print result
    return result
