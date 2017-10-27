import particle_swarm_optimization as pso

cuts = [3, 8, 15, 23]
min_max = [2, 25]
depth = 5

pso.run(cuts, min_max, depth)
