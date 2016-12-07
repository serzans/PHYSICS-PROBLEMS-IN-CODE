
import numpy as np
import matplotlib.pyplot as plt



x=np.linspace(-10,10,100)

r1=(x**2+0.05*(1+x**2))/(x+x**3)

r2=(x**2+0.15*(1+x**2))/(x+x**3)

plt.figure(1)
plt.plot(x,r1)
plt.xlabel("x")
plt.ylabel("r")
plt.savefig("saddle_node_1.png")

plt.figure(2)
plt.plot(x,r2)
plt.xlabel("x")
plt.ylabel("r")
plt.savefig("saddle_node_2.png")
