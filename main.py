import strong_fuzzy_partition as sfp
import particle_swarm_optimization as pso
from series_utilities import split_in_trap
from objective_function import minimize_slope_std
from sfp_plot import plot_trapeze_series

cuts_list = [[3, 8, 15, 23], [3, 8, 15, 23]]
minmax_list = [[2, 25], [2, 25]]
depth = 5


constant_slope = sfp.constant_slope(cuts_list, minmax_list)
print "Constant slope trap series {}".format(constant_slope)
plot_trapeze_series(cuts_list[0], minmax_list[0], split_in_trap(constant_slope[0]), depth)


optimal_series = pso.run(constant_slope, cuts_list, minmax_list, depth, minimize_slope_std)

dim = 1
plot_trapeze_series(cuts_list[dim], minmax_list[dim], split_in_trap(optimal_series[dim]), depth)