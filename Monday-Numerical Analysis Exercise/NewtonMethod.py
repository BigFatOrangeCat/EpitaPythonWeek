import math

def newton(a0, errorBd, maxIter, f, derivf):
	count = 0
	a1 = 0.0
	while errorBd < abs(f(a0)/df(a0)):
		a1 = a0 - f(a0)/df(a0)
		a0 = a1
		count += 1
		print(count, a1)
	return a1

f = lambda x: x**5 - x**4 + x - 1
df = lambda x: 5*x**4 -4*x**3 + 1
val = newton(1000000, 0.000001, 100, f, df)
print("Result is ", val)

"""
f = lambda x: x - math.e ** (-x)
df = lambda x: 1 + math.e ** (-x)
val = newton(1, 0.0000000001, 20, f, df)
print("Result is ", val)
"""