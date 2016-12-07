import matplotlib.pyplot as plt
import numpy as np

# Bohr magneton (J/T)
mu_B=9.274009994e-24

# Magnetic field strength (T)
B=1.0

# Planck constant
h=6.62607004e-34

# Frequency difference (Hz)
delta_f=28e9

# Energy difference
delta_E=h*delta_f


def lande_factor(S,L,J):
	return 3.0/2.0 + (S*(S+1)-L*(L+1))/(2.0*J*(J+1))

print delta_E/mu_B/B