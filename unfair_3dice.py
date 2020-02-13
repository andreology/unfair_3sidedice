import numpy as np
import matplotlib
import matplotlib.pyplot as plt

def ThreeSidedDie(p):
    N = 10000
    s = np.zeros( (N, 1))
    n = 3
    cs = np.cumsum(p)
    cp = np.append(0, cs)

    for j in range(0, N):
        r = np.random.rand()
        for k in range(0, n):
            if r > cp[k] and r <=cp[k+1]:
                d = k + 1
        s[j] = d
    #plotting results
    b = range(1, n + 2)
    sb = np.size(b)
    h1, bin_edges = np.histogram(s, bins=b)
    b1=bin_edges[0: sb -1]
    plt.close('all')
    prob = h1 / N
    plt.stem(b1, prob)
    #graphing labels for results
    plt.title('PMF for an unfair 3-sided die')
    plt.xlabel('Number on the face of the die')
    plt.ylabel('Probability')
    plt.xticks(b1)
p = np.array([0.3, 0.6, 0.1])
ThreeSidedDie(p)
