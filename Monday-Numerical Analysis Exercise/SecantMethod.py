import math


def secant(a0, a1, errorBd, maxIter, f):
	count = 0
	while abs(a1 - a0) > errorBd and count < maxIter :
		a2 = a1 - ((a1 - a0)/(f(a1) - f(a0))) * f(a1)
		a0 = a1
		a1 = a2
		count += 1
		print(count, a2)
	return a2


f = lambda x: x**5 - x**4 + x - 1
val = secant(0.9, 1.1, 0.0000000001, 20, f)
print("Result is ", val)

f = lambda x: x - math.e ** (-x)
val = secant(1, 1.5, 0.0000000001, 20, f)
print("Result is ", val)