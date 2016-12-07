import numpy as np
import matplotlib.pyplot as plt

r=0.3


x=[1.0]

for i in range(10):
	x.append(r*x[-1]*(1-x[-1]))

plt.plot(x)
plt.show()