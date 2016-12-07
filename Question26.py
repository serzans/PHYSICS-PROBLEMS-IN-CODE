
# Numerical calculation for an engine extracting heat between a hot reservoire of temperature T_1 and a cold reservoire of temperature T_2 to heat a body of temperature T_3.

# Set specific heat of material. Relative units this time.
C_p = 1.0

# Set initial temperatures (K).
# Hot reservoire.
T_1 =  300.0
# Cold reservoire.
T_2 = 100.0

T_3 = 300.0



# Initialise step size for taking heat away from the hot reservoire (K * relative unit).
dQ1 = 0.1

# Apply Clausius' statement as a while loop condition.
while T_1 > T_2:
	# Calculate Carnot thermal efficiency.
	eta = 1 - T_2/T_1

	# Work done by the ideal Carnot engine.
	W = eta * dQ1

	eta_2 = 1.0 - T_2/T_3

	CP_2 = 1/eta_2

	# Calculate waste heat
	dQ2 = (1 - eta) * dQ1
	dQ3 = CP_2 * W
	dQ2_prime = CP_2 * (W - 1)
	# Readjust the temperatures due to heat loss and heat gain in the reservoires.
	T_1 -= dQ1 
	T_2 += dQ2 - dQ2_prime
	T_3 += dQ3


print T_3