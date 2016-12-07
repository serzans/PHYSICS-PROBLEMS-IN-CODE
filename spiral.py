import turtle
import math

corinna = turtle.Turtle()
corinna.speed(1000)
corinna.pu()

n = 100


def isprime(c):
	flag = 1
	for l in range(2,int(math.sqrt(c))+1):
		if (c%l == 0):
			flag = 0
			break
	return flag

c = 1
for i in range(1,n):
	for j in range(2):
		for k in range(1,i):
			c += 1
			corinna.forward(10)
			if isprime(c):
				corinna.stamp()
		corinna.left(90)


