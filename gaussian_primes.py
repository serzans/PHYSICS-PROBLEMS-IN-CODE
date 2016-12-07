import numpy as np
# import matplotlib.pyplot as plt


def create_complex_integer_array(n):
	c=np.zeros((2*n+1,2*n+1),dtype=complex)
	for k in range(2*n+1):
		for l in range(2*n+1):
			c[k,l]+=1.0*(k-n)+1.0j*(l-n)
	return c


def generate_complex_shells(c):
	complex_shells=[]
	for i in range(10):
		



gaussian_primes=create_complex_integer_array(3)

# plt.matshow(gaussian_primes)
