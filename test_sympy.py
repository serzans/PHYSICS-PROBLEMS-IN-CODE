from sympy import *

x, y, z, t = symbols('x y z t')

print(solve([x*y - z, x - t], x, y))

print(solve(x*exp(x) - 1, x ))