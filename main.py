import strong_fuzzy_partition

cuts = [3, 8, 15, 23]
min_max = [2, 25]

computed_trapezes = strong_fuzzy_partition.build_trapezes_series(cuts, min_max)
res = [str(trapeze) for trapeze in computed_trapezes]

print 'cuts: ' + str(cuts)
print 'min-max: ' + str(min_max)
print res
