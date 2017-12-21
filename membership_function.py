from dataset_classifier import is_in_granule

A = 0
B = 1
C = 2
D = 3


def set_class_according_to_membership(dataset, trapezes, granules, cuts_list, minmax_list):
    for point in dataset:
        membership_value, granule = _get_membership(point, trapezes, granules)
        _set_class(point, granule, cuts_list, minmax_list)
    return dataset


def _get_membership(point, trapezes, granules):
    candidate_granule = []
    max = -1

    for j in range(len(granules)):
        associated_trapezes = _get_associated_trapezes(trapezes, granules[j])
        membership_list = []
        for i in range(len(associated_trapezes)):
            coord_membership = _get_coord_membership(point[i], associated_trapezes[i])
            # membership_x = _get_coord_membership(point[0], associated_trapezes[0])
            # membership_y = _get_coord_membership(point[1], associated_trapezes[1])
            membership_list.append(coord_membership)
        membership_value = min(membership_list)
        # membership_value = min(membership_x, membership_y)
        if max < membership_value:
            candidate_granule = granules[j]
            max = membership_value

    return max, candidate_granule


def _get_associated_trapezes(trapezes, granule):
    trapezes_list = []
    # if trapezes_list
    for i in range(len(granule) - 1):
        trapezes_list.append(trapezes[i][granule[i]-1])
    return trapezes_list


def _get_coord_membership(coord, trapeze):
    membership = 0
    if trapeze[A] < coord < trapeze[B]:
        membership = (coord - trapeze[A]) / float(trapeze[B] - trapeze[A])
    elif trapeze[B] <= coord <= trapeze[C]:
        membership = 1
    elif trapeze[C] < coord < trapeze[D]:
        membership = (coord - trapeze[D]) / float(trapeze[C] - trapeze[D])

    return membership


def _set_class(point, granule, cuts_list, minmax_list):
    if is_in_granule(point, granule, cuts_list, minmax_list):
        point.append(granule[-1])
    # return point.append(granule[-1]) if is_in_granule(point, granule, cuts_list, minmax_list)   else point.append("no class")
    return point
