import numpy as np
import matplotlib.pyplot as plt


r=np.linspace(0.01,0.5,100)

def root2(r):
	return (1.0+np.sqrt(1.0-4.0*r**2))/2.0/r


def root3(r):
	return (1.0-np.sqrt(1.0-4.0*r**2))/2.0/r


fp1=r*0.0
fp2=root2(r)
fp3=root3(r)


def stability(r,root):
	return -r+2.0*root/(1.0+root**2)**2


stability1=stability(r,fp1)
stability2=stability(r,fp2)
stability3=stability(r,fp3)


plt.figure(1)
plt.plot(r,stability1)
plt.title("Stability of fixed point 1")
plt.savefig("stability1.png")

plt.figure(2)
plt.plot(r,stability2)
plt.title("Stability of fixed point 2")
plt.savefig("stability2.png")

plt.figure(3)
plt.plot(r,stability3)
plt.title("Stability of fixed point 3")
plt.savefig("stability3.png")


x=np.linspace(-10,10)
def fixed_p_eqn(x):
	return x/(1+x**2)

plt.figure(4)
plt.plot(r,fp2)
plt.plot(r,fp3)
plt.title("Flows as function of r")
plt.savefig("flows_plot.png")


def r_with_s(x):
	return (x**2+0.15*(1+x**2))/(x+x**3)

plt.figure(5)
plt.plot(x,r_with_s(x))
plt.savefig("r_with_s.png")
