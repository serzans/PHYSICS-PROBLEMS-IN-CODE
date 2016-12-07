import numpy as np
import matplotlib.pyplot as plt

x=[np.pi]
y=[np.pi+0.0000000000001*np.sqrt(2)]

for i in range(40):
	x.append(10*(x[-1]-int(x[-1])))

for i in range(40):
	y.append(10*(y[-1]-int(y[-1])))

n=np.arange(len(x))

plt.plot(n,x)
plt.plot(n,y)
plt.xlabel("iteration $n$")
plt.ylabel("$x_n$")
plt.title("Decimal shift map, $x_0=\pi$")
plt.savefig("decimal_shift2.png")