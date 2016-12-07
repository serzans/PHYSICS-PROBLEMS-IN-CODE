import numpy as np
import random
from scipy import constants
from sympy import *


# Mass of particles
m=Symbol("m")

# Boltzmann constant
k_B=Symbol("k_B")

# Temperature of the distribution (K)
T=Symbol("T")

v=Symbol("v")

f_v=(m/2/pi/k_B/T)**(1.5)*4*pi*v**2*exp(-m*v**2/2/k_B/T)

print integrate(f_v,(v,0,oo))

# Normalise and calculate the cumulative probability

# n_particles=100

# particles=np.array((1,100))
