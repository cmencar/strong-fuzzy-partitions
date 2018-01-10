import membership_function as mf
import strong_fuzzy_partition as sfp
import particle_swarm_optimization as pso
import get_data as gd
from sfp_plot import trap_plot_2d
import time

start_time = time.time()

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

""" dummy data
cuts_list = [[6], [7, 10]]
minmax_list = [[2, 10], [3, 15]]
dataset = [[(3, 6), 'C1'], [(4, 5), 'C1'], [(5, 4), 'C1'], [(7, 9), 'C2'], [(8, 8), 'C2'], [(9, 9), 'C2'],
           [(3, 11), 'C1'], [(3, 15), 'C1'], [(4, 13), 'C1'], [(5, 11), 'C1'], [(5, 15), 'C1'], [(5, 13), 'C2'],
           [(10, 13), 'C1']]
"""

cuts_list = [[0.5], [0.4, 0.6]]
minmax_list = [[0.1, 0.8], [0.1, 0.9]]
granules_list = [[1, 1, 'C1'], [2, 2, 'C2'], [1, 3, 'C1']]
dataset = gd.get_data('data.csv')

constant_slope = sfp.constant_slope(cuts_list, minmax_list)
print "Constant slope trap series {}".format(constant_slope)
# trap_plot_2d(constant_slope, cuts_list, minmax_list)

max_iter = 10
optimal_series = pso.run(constant_slope, cuts_list, minmax_list, granules_list, dataset, mf.get_dataset_accuracy,
                         max_iter)
print "optimal series: {}".format(optimal_series)

print "Done in {} minutes".format((time.time() - start_time) / 60)

# trap_plot_2d(optimal_series, cuts_list, minmax_list)
