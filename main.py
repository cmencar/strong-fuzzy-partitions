import strong_fuzzy_partition as sfp
import particle_swarm_optimization as pso
import objective_function as obj
from sfp_plot import trap_plot_2d

cuts_list = [[3, 8, 15, 23], [3, 8, 15, 23]]
minmax_list = [[2, 25], [2, 25]]
depth = 5


constant_slope = sfp.constant_slope(cuts_list, minmax_list)
print "Constant slope trap series {}".format(constant_slope)
#trap_plot_2d(constant_slope, cuts_list, minmax_list)

# constant_slope_flat = [value for series in constant_slope for value in series]

max_iter = 100
optimal_series = pso.run(constant_slope, cuts_list, minmax_list, depth, obj.minimize_slope_std_flatten, max_iter)

trap_plot_2d(optimal_series, cuts_list, minmax_list)

