import csv
import numpy as np
from scipy import stats

reader = csv.reader(open("Dataset-film-data.csv", "rb"), delimiter=",")
data_as_list = list(reader)
D= [[] for _ in range(4)]
print D

for row in data_as_list:
	D[0].append(row[1])
	D[1].append(row[2])
	D[2].append(row[3])
	D[3].append(row[4])

for i in range(4):
	del D[i][0]

d = np.array(D).astype(np.float)
np.save('data_mat_D', d)


print "This is the normalized data matrix: \n"
a = b = [None] * 4
for i in range(4):
	a[i] = (d[i] - np.mean(d[i])) / np.std(d[i])
np.save('normalized_mat_A', a)
for i in range(4):
	b[i] = stats.zscore(d[i])
# print b

print "These are the max and mins for each feature: \n"
print "Max: \n"
print np.max(a,axis=1)
print "Min: \n"
print np.min(a,axis=1)

