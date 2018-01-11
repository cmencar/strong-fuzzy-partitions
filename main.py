import membership_function as mf
import strong_fuzzy_partition as sfp
import particle_swarm_optimization as pso
import get_data as gd
import series_utilities as util
import time

start_time = time.time()

""" dummy data
cuts_list = [[6], [7, 10]]
minmax_list = [[2, 10], [3, 15]]
dataset = [[(3, 6), 'C1'], [(4, 5), 'C1'], [(5, 4), 'C1'], [(7, 9), 'C2'], [(8, 8), 'C2'], [(9, 9), 'C2'],
           [(3, 11), 'C1'], [(3, 15), 'C1'], [(4, 13), 'C1'], [(5, 11), 'C1'], [(5, 15), 'C1']]
granules_list = [[1, 1, 'C1'], [2, 2, 'C2'], [1, 3, 'C1']]
"""

cuts_list = [[0.5], [0.4, 0.6]]
minmax_list = [[0.1, 0.8], [0.1, 0.9]]
granules_list = [[1, 1, 'C1'], [2, 2, 'C2'], [1, 3, 'C1']]
dataset = gd.get_data('data.csv')

# I need to multiply cuts and minmax for issues with decimal (less than 1) values
cuts_list = util.multiply(cuts_list)
minmax_list = util.multiply(minmax_list)

constant_slope = sfp.constant_slope(cuts_list, minmax_list)

# back to original values
cuts_list = util.divide(cuts_list)
minmax_list = util.divide(minmax_list)
constant_slope = util.divide(constant_slope)

print "Constant slope trap series {}".format(constant_slope)

max_iter = 10
optimal_series = pso.run(constant_slope, cuts_list, minmax_list, granules_list, dataset, mf.get_dataset_accuracy,
                         max_iter)
print "optimal series: {}".format(optimal_series)

print "Done in {} minutes".format((time.time() - start_time) / 60)
