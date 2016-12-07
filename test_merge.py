import numpy as np
from fractions import gcd
import matplotlib.pyplot as plt

def lcm(a,b):
	return (a*b)/gcd(a,b)

def merge_matrix_dims(A,B):
	dimx=lcm(np.shape(A)[0],np.shape(B)[0])
	dimy=lcm(np.shape(A)[1],np.shape(B)[1])

	xstep1=dimx/np.shape(A)[0]
	ystep1=dimy/np.shape(A)[1]
	xstep2=dimx/np.shape(B)[0]
	ystep2=dimy/np.shape(B)[1]

	# Initialise new matrices
	A_new=np.zeros((dimx,dimy))
	B_new=np.zeros((dimx,dimy))

	for i in range(np.shape(A)[0]):
		for j in range(np.shape(A)[1]):
			A_new[i*xstep1:i*xstep1+xstep1,j*ystep1:j*ystep1+ystep1]=A[i,j]

	for k in range(np.shape(B)[0]):
		for l in range(np.shape(B)[1]):
			B_new[k*xstep2:k*xstep2+xstep2,l*ystep2:l*ystep2+ystep2]=B[k,l]

	return (A_new,B_new)

def find_fast_electrons(A,B,E_min,c_min,cmax):
	return (A>=E_min) + (B>=c_min) + (B<=c_max)

x=np.eye(3)
y=np.array([[1,2],[3,4]])

print merge_matrix_dims(x,y)[0]
