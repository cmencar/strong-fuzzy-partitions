import strong_fuzzy_partition as sfp
import particle_swarm_optimization as pso
import objective_function as obj
from sfp_plot import trap_plot_2d
import time

start_time = time.time()

cuts_list = [[3, 8, 15, 23], [4, 7, 10]]
minmax_list = [[2, 25], [3, 15]]


constant_slope = sfp.constant_slope(cuts_list, minmax_list)
print "Constant slope trap series {}".format(constant_slope)
# trap_plot_2d(constant_slope, cuts_list, minmax_list)

max_iter = 10
optimal_series = pso.run(constant_slope, cuts_list, minmax_list, obj.minimize_slope_std, max_iter)
print "optimal series: {}".format(optimal_series)

print "Done in {} minutes".format((time.time() - start_time) / 60)

trap_plot_2d(optimal_series, cuts_list, minmax_list)


