import numpy as np
import matplotlib 
matplotlib.use('Agg')

import matplotlib.pyplot as plt
import pylab 
import scipy.stats as stats

d = np.load('data_mat_D.npy')

# Convert numpy array to list
list(d)
d = d.tolist()

# Pick bins and compute probability
bins = [[1, 5],[5, 6],[6,7]]

a1 = sum(bins[0][1] > numbers >= bins[0][0] for numbers in d[0])
a2 = sum(bins[1][1] > numbers >= bins[1][0] for numbers in d[0])
a3 = sum(bins[2][1] > numbers >= bins[2][0] for numbers in d[0])

a = [a1, a2, a3]


b1 = sum(bins[0][1] > numbers >= bins[0][0] for numbers in d[2])
b2 = sum(bins[1][1] > numbers >= bins[1][0] for numbers in d[2])
b3 = sum(bins[2][1] > numbers >= bins[2][0] for numbers in d[2])

b = [b1, b2, b3]

print stats.entropy(a, b)
print stats.entropy(b, a)