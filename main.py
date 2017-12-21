from base_generator import generate_base
from membership_function import set_class_according_to_membership
from dataset_classifier import classify_points
from accuracy_calculator import calculate_accuracy

# cuts_list = [[3, 8, 15, 23], [4, 7, 10]]
minmax_list = [[2, 25], [3, 15], [4, 45]]

# minmax_list = [[2, 25], [3, 15]]

"""
cuts_list = [[8, 16, 24], [6, 12]]
trapezes = [[[5, 5, 7, 9], [7, 9, 15, 17], [15, 17, 23, 25], [23, 25, 35, 35]],
            [[4, 4, 5, 7, ], [5, 7, 11, 13], [11, 13, 25, 25]]]
granules = [[2, 3, 'blue'], [4, 2, 'red']]
dataset = [[33, 18], [34, 5], [14, 15], [27, 9], [15, 8], [22, 20], [29, 5], [8, 18], [6, 17], [32, 14]]
"""

dataset, cuts_list, trapezes, granules = generate_base(minmax_list, 10, 2)
print "dataset", dataset
print "cuts", cuts_list
print "trapezes", trapezes
print "granules selected", granules

dataset = classify_points(dataset, granules, cuts_list, minmax_list)
print dataset
dataset = set_class_according_to_membership(dataset, trapezes, granules, cuts_list, minmax_list)
print dataset
print (calculate_accuracy(dataset))
