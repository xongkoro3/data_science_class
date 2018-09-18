import numpy as np

d = np.load('data_mat_D.npy')
r = np.corrcoef([d[0],d[1],d[2],d[3]])
print r