import numpy as np
import matplotlib 
matplotlib.use('Agg')

import matplotlib.pyplot as plt

d = np.load('data_mat_D.npy')

a = d[0,:]
b = d[2,:]

# percs = np.linspace(0,100,21)
# qn_a = np.percentile(a, percs)
# qn_b = np.percentile(b, percs)

# plt.plot(qn_a,qn_b, ls="", marker="o")

# x = np.linspace(np.min((qn_a.min(),qn_b.min())), np.max((qn_a.max(),qn_b.max())))
# plt.plot(x,x, color="k", ls="--")

# plt.show()
fig = plt.figure(1, figsize=(9, 6))

x = y = []
for i in range(0,100):
    x.append(np.percentile(a,i))
    y.append(np.percentile(b,i))
plt.scatter(x,y)
plt.xlabel("AvgRating_Website_1")
plt.ylabel("AvgRating_Website_3")

fig.savefig('fig5.png')
