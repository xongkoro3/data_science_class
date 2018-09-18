import numpy as np
import matplotlib 
matplotlib.use('Agg')

import matplotlib.pyplot as plt

d = np.load('data_mat_D.npy')

fig = plt.figure(1, figsize=(9, 6))

# Create an axes instance
ax = fig.add_subplot(111)

# Create the boxplot
bp = ax.boxplot(d[0,:])

fig.savefig('fig1.png', bbox_inches='tight')
