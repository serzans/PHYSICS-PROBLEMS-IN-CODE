
# Numerical calculation for an engine extracting heat between a hot reservoire of temperature T_1 and a cold reservoire of temperature T_2.

# Set specific heat of material (water in this case) J/(kg*K).
C_p = 4200.0

# Set initial temperatures (K).
# Hot reservoire.
T_1 =  373.0
# Cold reservoire.
T_2 = 273.0

# Initialise work variable (J/kg).
W = 0

# Initialise step size for taking heat away from the hot reservoire (J/kg).
dQ1 = 1
# In this case, take one Joule per one kilogram at a time.

# Apply Clausius' statement as a while loop condition.
while T_1 > T_2:
	# Calculate Carnot thermal efficiency.
	eta = 1 - T_2/T_1

	# Add work done by the ideal Carnot engine.
	W += eta * dQ1

	# Calculate waste heat
	dQ2 = (1 - eta) * dQ1

	# Readjust the temperatures due to heat loss and heat gain in the reservoires.
	T_1 -= dQ1 / C_p
	T_2 += dQ2 / C_p


# Average T_1 and T_2 to get the equilibrium temperature.
T_f = (T_1 + T_2) / 2.0

print 'Work = ' + str(W) + ' J/kg'