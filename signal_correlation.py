import numpy as np


def signal_correlation(a,b):
	# Normalised Fourier transforms
	a=a/np.sum(a)
	b=b/np.sum(b)
	a_fft_norm=np.fft.rfft(a)/np.sum(np.fft.rfft(a))
	b_fft_norm=np.fft.rfft(b)/np.sum(np.fft.rfft(b))

	# Correlation
	corr=np.correlate(a,b)

	# Integrate
	c=np.sum(corr)

	return c

x=np.linspace(0,1,1000)
y1=np.sin(x)
y2=np.sin(x-0.1)


print signal_correlation(y1,y2)
# Auto-correlation
print signal_correlation(y1,y1)