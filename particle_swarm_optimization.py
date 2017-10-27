from pyswarm import pso
import strong_fuzzy_partition as sfp
import series_utilities as util
from sfp_plot import plot_trapeze_series
from scipy.spatial.distance import cosine


def run(cuts, min_max, depth):
    def fitness_function(a_series):
        trap_series = util.generate_series(a_series, cuts, min_max)
        return util.get_slope_std(trap_series, depth)

    # Create constant slope vector, call it "seed", and extract only a for every trap
    seed = sfp.constant_slope(cuts, min_max)
    seed_a = util.extract_a_series(seed)
    print "seed: {}".format(seed)
    print "seed_a: {}\n".format(seed_a)

    # Compute bounds
    bounds = util.randomize_a_series(seed_a, cuts, min_max)
    lb = bounds[0]
    ub = bounds[1]
    print "lb: {}".format(lb)
    print "ub: {}".format(ub)

    # Run PSO
    optimal_a, optimal_func_out = pso(fitness_function, lb, ub)
    print "\nBest vector found: {}".format(optimal_a)
    print "Best slope found: {}".format(optimal_func_out)

    # Build optimal series using PSO output
    optimal_series = util.generate_series(optimal_a, cuts, min_max)
    print "\nOptimal series: {}".format(optimal_series)
    similarity_with_seed = 1 - cosine(optimal_series, seed)
    print "Solution's similarity with constant slope vector: {}\n".format(similarity_with_seed)

    plot_trapeze_series(cuts, min_max, util.split_in_trap(optimal_series), depth)
