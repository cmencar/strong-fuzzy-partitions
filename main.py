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
dataset = [[(3, 6), 'C1'], [(4, 5), 'C1'], [(5, 4), 'C1'], [(7, 9), 'C2'], [(8, 8), 'C2'], [(9, 9), 'C2'],
           [(3, 11), 'C1'], [(3, 15), 'C1'], [(4, 13), 'C1'], [(5, 11), 'C1'], [(5, 15), 'C1']]
granules_list = [[1, 1, 'C1'], [2, 2, 'C2'], [1, 3, 'C1']]
"""

""" punti sui bordi
cuts_list = [[5], [6, 8]]
minmax_list = [[2, 8], [3, 10]]
dataset = [[(4, 4.5), 'C1'], [(4, 5.5), 'C1'], [(5, 5), 'C1'], [(5, 6), 'C1'], [(5, 6.5), 'C2'], [(5, 7), 'C2'],
           [(5, 7.5), 'C2'], [(6, 7), 'C2'], [(3, 8), 'C1'], [(4, 8), 'C1'], [(5, 8), 'C1'], [(5, 9), 'C1'], [(4, 9.5),
                                                                                                              'C1']]
granules_list = [[1, 1, 'C1'], [2, 2, 'C2'], [1, 3, 'C1']]
"""

""" punti rumorosi sui bordi
cuts_list = [[5], [5, 8]]
minmax_list = [[2, 8], [3, 9]]
dataset = [[(4, 4.5), 'C1'], [(4, 5), 'C2'], [(5, 5), 'C2'], [(5, 4.5), 'C2'], [(5, 6.5), 'C2'], [(5.5, 7), 'C1'],
           [(7.5, 5), 'C1'], [(5, 8), 'C1'], [(3.5, 8), 'C2'], [(5, 8.5), 'C2']]
granules_list = [[1, 1, 'C1'], [2, 2, 'C2'], [1, 3, 'C1']]
"""

# punti distribuiti uniformemente

cuts_list = [[0.5], [0.4, 0.6]]
minmax_list = [[0, 1], [0, 1]]
granules_list = [[1, 1, 'C1'], [2, 2, 'C2'], [1, 3, 'C1']]
dataset = gd.get_data('data.csv')


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
    mf.get_dataset_accuracy(constant_slope_a_seeds, cuts_list, minmax_list, granules_list, dataset))
print 'Constant slope accuracy: {}'.format(constant_slope_accuracy)

max_iter = 10
optimal_series = pso.run(a_seeds, cuts_list, minmax_list, granules_list, dataset, mf.get_dataset_accuracy,
                         max_iter)
print "optimal series: {}".format(optimal_series)

trap_plot_2d(optimal_series, cuts_list, minmax_list)

print "Done in {} minutes".format((time.time() - start_time) / 60)
