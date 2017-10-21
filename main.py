import strong_fuzzy_partition as sfp
from trap_utility import split_in_trap
from sfp_plot import plot_trapeze_series

cuts = [3, 8, 15, 23]
min_max = [2, 25]

trap_series = sfp.constant_slope(cuts, min_max)

print 'cuts:\n' + str(cuts)
print 'min-max:\n' + str(min_max)
print 'trapeze series:\n'
print trap_series

random_series = sfp.randomize_slope(trap_series)
random_slope = sfp.get_slope_std(random_series)
constant_slope = sfp.get_slope_std(trap_series)
print "random slope: {}".format(random_slope)
print "constant slope: {}".format(constant_slope)

# Plot
series_split = split_in_trap(trap_series)
plot_trapeze_series(cuts, min_max, series_split, 5)

random_split = split_in_trap(random_series)
plot_trapeze_series(cuts, min_max, random_split, 5)
