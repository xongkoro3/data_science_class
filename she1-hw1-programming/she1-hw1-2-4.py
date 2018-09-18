import numpy as np
import matplotlib 
matplotlib.use('Agg')

import matplotlib.pyplot as plt

# Scatterplot
d = np.load('data_mat_D.npy')

action = (d[0,0:50], d[2, 0:50])
romance = (d[0,50:100], d[2, 50:100])
comedy = (d[0,100:150], d[2, 100:150])

data = (action, romance, comedy)

colors = ("red", "yellow", "blue")
groups = ("action", "romance", "comedy")


fig = plt.figure(1, figsize=(9, 6))
ax = fig.add_subplot(1, 1, 1, axisbg="1.0")

for data, color, group in zip(data, colors, groups):
    x, y = data
    ax.scatter(x, y, alpha=0.5, c=color, label=group)

plt.xlabel('AVGRATING_WEBSITE_1')
plt.ylabel('AVGRATING_WEBSITE_3')
plt.legend(loc=2)

fig.savefig('fig4.png')
