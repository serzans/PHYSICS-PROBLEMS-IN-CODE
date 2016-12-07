import numpy as np
import matplotlib.pyplot as plt


ev=1.6e-19

E=17.52*1e3*ev
print E

m_e=9.10938356e-31

c=3e8

theta=np.linspace(0,np.pi/2-0.001,100)
print theta
print np.cos(theta)
print 1-np.cos(theta)

E_p=E/(1+(1-np.cos(theta))*E/m_e/c**2)
print (1-np.cos(theta)*E/m_e/c**2)
print E_p
plt.plot(theta,E_p/1.0e3/ev)
plt.xlabel("$\Theta$, radians")
plt.ylabel("Scattered Photon Energy, keV")
plt.title("Scattered Energy as Function of Angle")
plt.show()