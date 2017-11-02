import series_utilities as util


def minimize_slope_std(a_series, *args):
    def split_series_for_dimension(a_series, cuts_list):
        result = []
        for i in range(0, len(cuts_list)):
            k = len(cuts_list[i])
            result.append(a_series[0:k])
            a_series = a_series[k:]
        return result

    def rebuild_series(a_series_split, cuts_list, minmax_list):
        result = []
        for i in range(0, len(a_series_split)):
            trap_series = util.generate_series(a_series_split[i], cuts_list[i], minmax_list[i])
            result.append(trap_series)
        return result

    cuts_list, minmax_list, depth = args
  
    a_series_split = split_series_for_dimension(a_series, cuts_list)
    trap_series_split = rebuild_series(a_series_split, cuts_list, minmax_list)
    std_list = [util.get_slope_std(trap_series, depth) for trap_series in trap_series_split]
    result = sum(std_list) / len(std_list)
    return result
