import matplotlib.pyplot as plt
import numpy as np
import math


A = np.zeros((100,100))

# Define range of window.
x_max = 1.0
y_max = 1.0
# Define temperature at boundary where y = 0.
T_0 = 10.0

# Calculate step sizeson x and y.
dx = x_max / (A.shape[0] - 1)
dy = y_max / (A.shape[1] - 1)

def temperature(x,y,n,L,T_0):
	# Avoid even values of n.
	if n % 2 == 1:
		return T_0 * 4 / (n*math.pi) * math.sin(n*math.pi*x/L) * math.exp(-n*math.pi*y/L)
	else:
		return 0

# Iterate over integer values of n.
for n in range(30):
	# Loop through the matrix.
	for i in range(A.shape[0]):
		for j in range(A.shape[1]):
			# x and y implicitly defined by matrix indices.
			x = i * dx
			y = j * dy
			A[i][j] += temperature(x,y,n,x_max,T_0)


plt.matshow(A)
plt.show()