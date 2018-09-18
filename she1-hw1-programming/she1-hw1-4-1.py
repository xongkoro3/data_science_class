import numpy as np
import matplotlib 
matplotlib.use('Agg')
from sklearn.decomposition import PCA 

import matplotlib.pyplot as plt

a = np.load('normalized_mat_A.npy')
a = np.around(a,2)
a_formatted = np.transpose(a)

# PCA
pca = PCA(n_components=3)
features_pca = pca.fit_transform(a_formatted)
eigenvalues = pca.explained_variance

print "eigenvalues: " + str(eigenvalues)

action = (features_pca[:50,:1],features_pca[:50,1:2])
romance = (features_pca[50:100,:1],features_pca[50:100,1:2])
comedy = (features_pca[100:150,:1],features_pca[100:150,1:2])
data = (action, romance, comedy)
colors = ("red", "yellow", "blue")
groups = ("action", "romance", "comedy")
markers = ("s", "*", "p")

fig = plt.figure(figsize=(9,6))
ax = fig.add_subplot(1, 1, 1, axisbg="1.0")

# plt.scatter(features_pca[:,0], features_pca[:,1],
#             c=colors, alpha=0.5)

for data, color, group, marker in zip(data, colors, groups, markers):
    x, y = data
    ax.scatter(x, y, alpha=0.5, c=color, marker=marker, label=group)

plt.xlabel('PC 1')
plt.ylabel('PC 2') 
plt.legend(loc=2)

fig.savefig('fig7a.png')

