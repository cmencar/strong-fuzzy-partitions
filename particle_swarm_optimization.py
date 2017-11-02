from pyswarm import pso
import strong_fuzzy_partition as sfp
import series_utilities as util
from sfp_plot import plot_trapeze_series
from scipy.spatial.distance import cosine

LOWER = 0
UPPER = 1


def run(seeds, cuts, min_max, depth, fitness_function):
    # Optimization process needs only "a" vertex from every trap
    a_seeds = [util.extract_a_series(seed) for seed in seeds]

    # Compute bounds. Bounds are the search space for the optimization process
    # It iterates over the number of data dimensions.
    lb = []
    ub = []
    for i in range(0, len(a_seeds)):
        bounds = util.compute_bounds(a_seeds[i], cuts[i], min_max[i])
        [lb.append(b) for b in bounds[LOWER]]
        [ub.append(b) for b in bounds[UPPER]]

    # Run PSO
    args = (cuts, min_max, depth)
    optimal_a, optimal_func_out = pso(fitness_function, lb, ub, args=args, maxiter=10000)
    print "Best fitnessfunc's output found: {}".format(optimal_func_out)
    print "Best fiting data: {}".format(optimal_a)

    # Rebuild trap series for each dimension
    optimal_series = []
    for i in range(0, len(cuts)):
        k = len(cuts[i])
        trap_series = util.generate_series(optimal_a[:k], cuts[i], min_max[i])
        optimal_series.append(trap_series)
        optimal_a = optimal_a[k:]

    return optimal_series
