import numpy as np

A=np.array([[1,2,3,4],[5,6,7,8],[9,10,11,12],[13,14,15,16],[5,4,2,1],[7,2,5,1]])


# A=np.array([[1,2],[2,2],[3,2],[4,2],[5,2],[6,2],[7,2]])

U=np.zeros((np.shape(A)[0]/2,np.shape(A)[0]))

for i in range(np.shape(A)[0]/2):
	U[i,2*i]=1

print U

print np.dot(U,A)