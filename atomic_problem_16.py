import numpy as np
import matplotlib.pyplot as plt

# Planck's constant (J*s)
h=6.62607004e-34

# Speed of light (m/s)
c=299792458

# Permeability of free space
mu_0=1.25663706e-6

# Bohr magneton (J/T)
mu_B=9.274009994e-24

# Transition wavelength 5p56s to 5p56p (m)
lambda_0=494e-9

# Wavenumber of 5p56s to 5p56p transition
k_0=2.0*np.pi/lambda_0

# Energy of 5p56s to 5p56p transition
E_0=h*c/2.0/np.pi*k_0

# Wavenumber shifts (m^-1). Uncertainty in each value is of order 0.1 (m^-1)
delta_k=np.array([0.0,8.1,19.5,33.7,51.3])

# For the wavenumber shift 0.0, F=I+J

# For highest wavenumber shift, F=0


print (19.5-33.7)/(33.7-51.3)

# delta E ~ delta k -> 

# from sympy import solve_poly_system
# from sympy.abc import i,j
# print solve_poly_system([-i*(i+1)-j*(j+1)+51.3,1/2*(1/2+1)-i*(i+1)-j*(j+1)+33.7],i,j)


# Find I, find J


def H_HFS(F,I,J):
	A_j=1.0
	return A_j*(F*(F+1)-I*(I+1)-J*(J+1)) 

F=np.array([4.0,3.0,2.0,1.0,0.0])

plt.figure("Experimental")
plt.plot(F,delta_k,"bx")
plt.show()

plt.figure("Theoretical")
plt.plot(F,H_HFS(F,,1.5),"rx")
plt.show()




