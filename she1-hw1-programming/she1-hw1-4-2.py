import numpy as np
import matplotlib 
matplotlib.use('Agg')
import matplotlib.pyplot as plt
from scipy.linalg import svd

# SVD
a = np.load('normalized_mat_A.npy')
a = np.around(a,2)
a_formatted = np.transpose(a)
print a_formatted

U,S,V = svd(a_formatted)
print U
print S
print V

action = (U[:50,:1],U[:50,1:2])
romance = (U[50:100,:1],U[50:100,1:2])
comedy = (U[100:150,:1],U[100:150,1:2])
data = (action, romance, comedy)
colors = ("red", "yellow", "blue")
groups = ("action", "romance", "comedy")
markers = ("s", "*", "p")

fig = plt.figure(figsize=(9,6))
ax = fig.add_subplot(1, 1, 1, axisbg="1.0")

for data, color, group, marker in zip(data, colors, groups, markers):
    x, y = data
    ax.scatter(x, y, alpha=0.5, c=color, marker=marker, label=group)

plt.legend(loc=2)

fig.savefig('fig8.png')
