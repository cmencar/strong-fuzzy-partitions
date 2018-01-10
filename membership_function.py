import series_utilities as util
import get_data as gd
import objective_function as obj

A = 0
B = 1
C = 2
D = 3


def get_dataset_accuracy(a_series, *args):
    cuts_list, minmax_list, granules, dataset = args
    num_good_classification = 0
    print 's', a_series
    a_series_split = obj.split_series_for_dimension(a_series, cuts_list)
    trap_series_split = obj.rebuild_series(a_series_split, cuts_list, minmax_list)
    trapezes = util.recreate_trapezes(trap_series_split)
    for point in dataset:
        membership_value, granule = _get_membership(point, trapezes, granules)
        if point[-1] == granule[-1] and membership_value > 0:
            num_good_classification = num_good_classification + 1
        accuracy_perc = float(num_good_classification) / len(dataset) * 100
    return -accuracy_perc


def _get_membership(point, trapezes, granules):
    candidate_granule = []
    max = -1

    for granule in granules:
        associated_trapezes = _get_associated_trapezes(trapezes, granule)
        membership_list = []
        for i in range(len(point[0])):
            coord_membership = _get_coord_membership(point[0][i], associated_trapezes[i])
            membership_list.append(coord_membership)
        membership_value = min(membership_list)
        if max < membership_value:
            candidate_granule = granule
            max = membership_value
    return max, candidate_granule


def _get_associated_trapezes(trapezes, granule):
    trapezes_list = []
    for i in range(len(granule) - 1):
        trapezes_list.append(trapezes[i][granule[i] - 1])
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
