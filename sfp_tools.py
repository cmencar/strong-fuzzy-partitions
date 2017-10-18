def init_population(seed, n):
    population = []
    for i in range(0, n):
        new_item = _generate_random_vec_series(seed)
        population.append(new_item)
    return population


def _generate_random_vec_series(seed):
    from random import uniform

    vec = seed[3:-1]
    for i in range(1, len(vec) - 1):
        vec[i] = uniform(vec[i - 1], vec[i + 1])
    return seed[0:3] + vec + [seed[-1]]


test_seed = [0, 0, 2, 2, 2.75, 3.25, 7.75, 8.25, 14.75, 15.25, 22.75, 23.25, 25, 25]
population = init_population(test_seed, 3)
print population


