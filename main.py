from base_generator import generate_base
from membership_function import set_class_according_to_membership
from dataset_classifier import classify_points
from accuracy_calculator import calculate_accuracy
import strong_fuzzy_partition as sfp
import particle_swarm_optimization as pso
import objective_function as obj
from sfp_plot import trap_plot_2d
import time

start_time = time.time()

# cuts_list = [[3, 8, 15, 23], [4, 7, 10]]
# minmax_list = [[2, 25], [3, 15]]

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
"""

cuts_list = [[0.5], [0.4, 0.6]]
minmax_list = [[0.1, 0.8], [0.1, 0.9]]
granules_list = [[1, 1, 'C1'], [2, 2, 'C2'], [1, 3, 'C1']]

constant_slope = sfp.constant_slope(cuts_list, minmax_list)
print "Constant slope trap series {}".format(constant_slope)
# trap_plot_2d(constant_slope, cuts_list, minmax_list)

max_iter = 10
optimal_series = pso.run(constant_slope, cuts_list, minmax_list, obj.minimize_slope_std, max_iter)
print "optimal series: {}".format(optimal_series)

print "Done in {} minutes".format((time.time() - start_time) / 60)

trap_plot_2d(optimal_series, cuts_list, minmax_list)
