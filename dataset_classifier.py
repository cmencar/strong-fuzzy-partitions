MIN = 0
MAX = 1


def classify_points(dataset, granules, cuts_list, minmax_list):
    assert len(cuts_list) == len(minmax_list)

    # for granule in granules:
    #   for point in dataset:
    for point in dataset:
        for granule in granules:
            if is_in_granule(point, granule, cuts_list, minmax_list):
                point.append(granule[-1])
                break
        # else:
        #    point[2] = "no class"
    return dataset


def is_in_granule(point, granule, cuts_list, minmax_list):
    intervals = _get_all_intervals(granule, cuts_list, minmax_list)
    for i in range(len(intervals)):
        if not intervals[i][0] <= point[i] <= intervals[i][1]:
            return False
    return True


def _get_all_intervals(granule, cuts_list, minmax_list):
    intervals = []
    for i in range(len(granule) - 1):
        interval = _get_single_interval(granule[i], cuts_list[i], minmax_list[i])
        intervals.append(interval)
    return intervals


def _get_single_interval(slot_idx, cuts_list, minmax_list):
    assert (1 <= slot_idx <= len(cuts_list) + 1)

    intervals = [minmax_list[MIN]] + cuts_list + [minmax_list[MAX]]
    return [intervals[slot_idx - 1], intervals[slot_idx]]
