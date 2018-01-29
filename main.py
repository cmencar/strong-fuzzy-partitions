import membership_function as mf
import strong_fuzzy_partition as sfp
import particle_swarm_optimization as pso
import get_data as gd
import series_utilities as util
from sfp_plot import trap_plot_2d
import time

start_time = time.time()

""" punti al centro
cuts_list = [[6], [7, 10]]
minmax_list = [[2, 10], [3, 15]]
dataset = gd.get_data('dataset/center_data.csv')
granules_list = [[1, 1, 'C1'], [2, 2, 'C2'], [1, 3, 'C1']]
print dataset
"""
""" punti sui bordi
cuts_list = [[5], [6, 8]]
minmax_list = [[2, 8], [3, 10]]
dataset = gd.get_data('dataset/edge_data.csv')
granules_list = [[1, 1, 'C1'], [2, 2, 'C2'], [1, 3, 'C1']]
print dataset
"""

""" punti rumorosi sui bordi
cuts_list = [[5], [5, 8]]
minmax_list = [[2, 8], [3, 9]]
dataset = gd.get_data('dataset/edge_noisy_data.csv')
granules_list = [[1, 1, 'C1'], [2, 2, 'C2'], [1, 3, 'C1']]
print dataset
"""

# punti distribuiti uniformemente
cuts_list = [[0.5], [0.4, 0.6]]
minmax_list = [[0, 1], [0, 1]]
granules_list = [[1, 1, 'C1'], [2, 2, 'C2'], [1, 3, 'C1']]
dataset = gd.get_data('dataset/uniform_data.csv')
print dataset

constant_slope = sfp.constant_slope(cuts_list, minmax_list)

print "Constant slope trap series {}".format(constant_slope)

# trap_plot_2d(constant_slope, cuts_list, minmax_list)

# Optimization process needs only "a" vertex from every trap
seeds = util.to_linear_series(constant_slope, len(cuts_list))
print 'seeds: {}'.format(seeds)
a_seeds = [util.extract_a_series(seed) for seed in seeds]
print "a_seeds {}".format(a_seeds)

constant_slope_a_seeds = util.to_a_series(a_seeds)

constant_slope_accuracy = -(
    mf.calculate_dataset_accuracy(constant_slope_a_seeds, cuts_list, minmax_list, granules_list, dataset))
print 'Constant slope accuracy: {}'.format(constant_slope_accuracy)

max_iter = 100
optimal_series = pso.run(a_seeds, cuts_list, minmax_list, granules_list, dataset, mf.calculate_dataset_accuracy,
                         max_iter)
print "optimal series: {}".format(optimal_series)

trap_plot_2d(optimal_series, cuts_list, minmax_list)

print "Done in {} minutes".format((time.time() - start_time) / 60)
