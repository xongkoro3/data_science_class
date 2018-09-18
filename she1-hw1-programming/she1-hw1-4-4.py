import numpy as np
import matplotlib 
matplotlib.use('Agg')
import matplotlib.pyplot as plt
from scipy.linalg import svd
import math
from sklearn.preprocessing import normalize
# propagation
def load_data():
	a = np.load('normalized_mat_A.npy')
	a = np.around(a,2)
	global a_formatted
	a_formatted = np.transpose(a)

	# Normalize as suggested in the question
	global u_0
	u_0 = normalize(a_formatted)
	global v_0
	v_0 = normalize(np.dot(np.transpose(a_formatted),u_0))


# Recursive function to approximate u and v
def appro(u,v,c):
    # global counter
    if c == 100:
    	result_u = np.around(u,2)
        result_v = np.around(v,2)
        # print approximate results
        print "\n+++++++++++++++++++++++++++++++++++++++++++++++++++++++++"
        print "This is v: \n"
        print result_v 
        print "\n+++++++++++++++++++++++++++++++++++++++++++++++++++++++++"
        print "This is u: \n"
        print result_u
        print "\n+++++++++++++++++++++++++++++++++++++++++++++++++++++++++"
        return 
    c+=1
    
    u_n = normalize(np.dot(a_formatted,v))
    v_n = normalize(np.dot(np.transpose(a_formatted),u_n))

    appro(u_n,v_n,c) # recursive call
    return 


def main():
	load_data()
	appro(u_0,v_0,0)
  
if __name__== "__main__":
	main()
