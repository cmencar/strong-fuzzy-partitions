import random

# div_factor should be at least 10 times less than the difference between m and M
DIV_FACTOR = 10

SLOPE = 0.05

CLASSES = ['green', 'red', 'blue']


def generate_base(minmax_list, num_examples, num_granules):
    dataset = generate_dataset(minmax_list, num_examples)
    cuts_list = generate_cuts(minmax_list)
    trapezes = create_trapezes(cuts_list, minmax_list)
    granules = select_granules(cuts_list, num_granules)
    return dataset, cuts_list, trapezes, granules


# generates points in the space in a random fashion in the format: [[coord_x, coord_y, ... , coord_n], [...], ...]
def generate_dataset(minmax_list, num_examples):
    dataset = []
    num_dimensions = len(minmax_list)
    for i in range(num_examples):
        point = []
        for j in range(num_dimensions):
            minimum = minmax_list[j][0]
            maximum = minmax_list[j][1]
            dim_value = random.randint(minimum, maximum)
            # dim_value = round(random.uniform(minimum, maximum), 2)
            point.append(dim_value)
        dataset.append(point)
    return dataset


# generates cuts according to a div factor and the range of min and max for each dimension
def generate_cuts(minmax_list):
    all_cuts = []
    for i in range(len(minmax_list)):
        dimension_cuts = []
        min_max_range = minmax_list[i][1] - minmax_list[i][0]
        num_cuts = min_max_range / DIV_FACTOR if (min_max_range / DIV_FACTOR) > 0 else 1
        sum_factor = minmax_list[i][0] + num_cuts
        cut = sum_factor
        for j in range(num_cuts):
            dimension_cuts.append(cut)
            cut = cut + sum_factor
        dimension_cuts = sorted(dimension_cuts)
        all_cuts.append(dimension_cuts)
    return all_cuts


# creates trapezes according to cuts, m and M
def create_trapezes(cuts_list, minmax_list):
    trapezes_list = []
    for i in range(len(cuts_list)):
        trapezes_series = []
        min = minmax_list[i][0]
        max = minmax_list[i][1]
        first_trapeze = [min, min, cuts_list[i][0] - SLOPE, cuts_list[i][0] + SLOPE]
        trapezes_series.append(first_trapeze)
        for j in range(1, len(cuts_list[i])):
            single_trapeze = [cuts_list[i][j - 1] - SLOPE, cuts_list[i][j - 1] + SLOPE, cuts_list[i][j] - SLOPE,
                              cuts_list[i][j] + SLOPE]
            trapezes_series.append(single_trapeze)
        last_trapeze = [cuts_list[i][-1] - SLOPE, cuts_list[i][-1] + SLOPE, max, max]
        trapezes_series.append(last_trapeze)
        trapezes_list.append(trapezes_series)
        if len(minmax_list) < 2:
            trapezes_list = [item for sublist in trapezes_list for item in sublist]
    return trapezes_list


# randomly choose a certain number of granules to be evaluated and randomly set a class
def select_granules(cuts_list, num_granules):
    granules = []
    while len(granules) < num_granules:
        granule = []
        for i in range(len(cuts_list)):
            num_dimension_granules = len(cuts_list[i]) + 1
            granule.append(random.randint(1, num_dimension_granules))
        granule = _set_class(granule)
        granules.append(granule)
    return granules


def _set_class(granule):
    random_int = random.randint(0, len(CLASSES) - 1)
    granule.append(CLASSES[random_int])
    return granule
