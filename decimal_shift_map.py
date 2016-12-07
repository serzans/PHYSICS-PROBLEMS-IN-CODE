import numpy as np
import matplotlib.pyplot as plt

x=[np.pi]

for i in range(40):
	x.append(10*(x[-1]-int(x[-1])))

n=np.arange(len(x))

plt.plot(n,x)
plt.xlabel("iteration $n$")
plt.ylabel("$x_n$")
plt.title("Decimal shift map, $x_0=\pi$")
plt.savefig("decimal_shift.png")