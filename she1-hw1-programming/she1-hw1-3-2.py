import numpy as np
from scipy import stats

a = np.load('normalized_mat_A.npy')
r = np.corrcoef([a[0],a[1],a[2],a[3]])

print r