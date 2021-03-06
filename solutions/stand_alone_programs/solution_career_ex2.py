import matplotlib.pyplot as plt
import numpy as np
from discrete_rv import discreteRV
from career import *
from compute_fp import compute_fixed_point

wp = workerProblem()
v_init = np.ones((wp.N, wp.N))*100
v = compute_fixed_point(bellman, wp, v_init)
optimal_policy = get_greedy(wp, v)
F = discreteRV(wp.F_probs)
G = discreteRV(wp.G_probs)

def gen_first_passage_time():
    t = 0
    i = j = 0  
    theta_index = []
    epsilon_index = []
    while 1:
        if optimal_policy[i, j] == 1:    # Stay put
            return t
        elif optimal_policy[i, j] == 2:  # New job
            j = int(G.draw())
        else:                            # New life
            i, j  = int(F.draw()), int(G.draw())
        t += 1

M = 25000 # Number of samples
samples = np.empty(M)
for i in range(M): 
    samples[i] = gen_first_passage_time()
print np.median(samples)
