import series_utilities as util
import base_generator as bg
import get_data as gd

A = 0
B = 1
C = 2
D = 3


def get_dataset_accuracy(dataset, cuts_list, minmax_list, granules):
    num_good_classification = 0
    trapezes = bg.create_trapezes(cuts_list, minmax_list)
    for point in dataset:
        membership_value, granule = _get_membership(point, trapezes, granules)
        if point[-1] == granule[-1]:
            num_good_classification = num_good_classification + 1
        accuracy_perc = float(num_good_classification) / len(dataset) * 100
    return accuracy_perc


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


# testing
dataset = gd.get_data('data.csv')
print dataset
cuts_list = [[0.5], [0.4, 0.6]]
minmax_list = [[0.1, 0.8], [0.1, 0.9]]
trapezes_list = [[[0.1, 0.1, 0.45, 0.55], [0.45, 0.55, 0.8, 0.8]],
                 [[0.1, 0.1, 0.35, 0.45], [0.35, 0.45, 0.55, 0.65], [0.55, 0.65, 0.9, 0.9]]]
granules_list = [[1, 1, 'C1'], [2, 2, 'C2'], [1, 3, 'C1']]

print get_dataset_accuracy(dataset, cuts_list, minmax_list, granules_list), '%'
