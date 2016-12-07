from sympy import *

t=Symbol("t")
k=Symbol("k")
m=Symbol("m")
b=Symbol("b")

f, g, y = symbols('f g y', cls=Function)

# # f(x).diff(x, x) + f(x)

# # 1st derivative
# print dsolve(f(x).diff(x) - f(x), f(x))

# # 2nd derivative
# print dsolve(f(x).diff(x,x) + f(x), f(x))

# # 4th derivative
# print dsolve(f(x).diff(x,x,x,x) + f(x), f(x))


# SHO
print dsolve(m*y(t).diff(t,t)+k*y(t),y(t))

# Damped harmonic oscillator
print dsolve(m*y(t).diff(t,t)+b*y(t).diff(t)+k*y(t),y(t))


# Forced harmonic oscillator?


# Figure out how to give boundary conditions!!!
