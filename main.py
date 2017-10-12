import strong_fuzzy_partition
import sfp_plot

cuts = [3, 8, 15, 23]
min_max = [2, 25]

computed_trapezes = strong_fuzzy_partition.build_trapezes_series(cuts, min_max)
res = [str(trapeze) for trapeze in computed_trapezes]

print 'cuts:\n' + str(cuts)
print 'min-max:\n' + str(min_max)
print 'trapeze series:\n'
print res

sfp_plot.plot_trapeze_series(cuts, min_max, computed_trapezes, depth=5)
