import numpy as np
import matplotlib 
matplotlib.use('Agg')

import matplotlib.pyplot as plt

d = np.load('data_mat_D.npy')
action = np.mean(d[0,0:50])
romance = np.mean(d[0,50:100])
comedy = np.mean(d[0,100:150])

movies = ('action', 'romance', 'comedy')
y_pos = np.arange(len(movies))
performance = [action,romance,comedy]

plt.bar(y_pos, performance, align='center')
plt.xticks(y_pos, movies)
plt.ylabel('Avg ratings')
plt.title('Movies')

fig = plt.figure(1, figsize=(9, 6))
fig.savefig('fig3.png')
