from math import *

N = 2

while True:
	if abs(log(factorial(N)) - N*log(N) + N) / log(factorial(N)) <= 0.02:
		print N
		break
	print abs(log(factorial(N)) - N*log(N) + N) / log(factorial(N))
	N+=1
