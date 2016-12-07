import numpy as np
import matplotlib.pyplot as plt

x=np.linspace(0,2,100)

a=np.sin(x)
b=(np.copy(a))
for i in range(10,20):
	b[i]=1

c=(np.copy(a))
for j in range(10,20):
	c[i]=0

print np.correlate(a,b)
print np.correlate(a,c)

plt.plot(x,a)
plt.plot(x,b)
plt.plot(x,c)
plt.show()


import wave

f1=wave.open("soundtest1.wav","r")
print f1
f2=wave.open("soundtest2.wav","r")
f3=wave.open("soundtest3.wav","r")