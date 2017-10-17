import sfp_generation
import sfp_plot

cuts = [3, 8, 15, 23]
min_max = [2, 25]

trap_series = sfp_generation.constant_slope(cuts, min_max)
trap_series_vec = trap_series.vectorize()

print 'cuts:\n' + str(cuts)
print 'min-max:\n' + str(min_max)
print 'trapeze series:\n'
print trap_series_vec

sfp_plot.plot_trapeze_series(cuts, min_max, trap_series, depth=5)
