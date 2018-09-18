import numpy as np
import matplotlib 
matplotlib.use('Agg')

import matplotlib.pyplot as plt

d = np.load('data_mat_D.npy')
plt.hist(d[2,:], bins=10)
print d[2,:]
fig = plt.figure(1, figsize=(9, 6))
fig.savefig('fig2a.png')
