import numpy as np
(x,y) = (4,5)
A = np.zeros((x,y), dtype=np.int)

for i in range(x):
	for j in range(y):
		A[i,j] = (i+j)^2



print A


