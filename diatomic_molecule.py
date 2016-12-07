import math

# Proton mass (kg)
m_p = 1.6726219e-27

# Reduced mass
mu = m_p * 48.0 / 7.0

m = 28 * m_p

# Frequencies (Hz)
f1 = 461.04077e9
f2 = 4115.6055e9

# Planck constants (J * s)
h = 6.62607004e-34
h_bar = h / (2 * math.pi)

def energy(l,I):
	return h_bar**2 * l * (l + 1) / (2 * I)

def distance(l1,l2,f):
	x = h_bar**2 / (2 * mu * h * f) * (l2*(l2+1)-l1*(l1+1))
	return math.sqrt(x)

# Intra-nuclear space
s1 = distance(3,4,f1)
s2 = distance(35,36,f2)

# Moments of inertia
I1 = mu * s1**2
I2 = mu * s2**2

F1 = mu * s1 * 2 * energy(3,I1) / I1
F2 = mu * s1 * 2 * energy(36,I2) / I2

k = (F2 - F1)/(s2-s1)

print k
print s1,s2
print math.sqrt(k/(mu))/(2*math.pi)

